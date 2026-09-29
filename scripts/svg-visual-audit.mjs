#!/usr/bin/env node
// svg-visual-audit.mjs — semantic + geometric visual audit for textbook figure SVGs.
// Checks for bad subscripts/superscripts, broken math notation, and text overflow.
// For each defective SVG, calls the Claude API to propose XML fixes, applies them,
// and queues them for re-render via svg-to-png.mjs.
//
// Usage:
//   node SCRIPTS/svg-visual-audit.mjs                    # audits ./images, fixes in place
//   node SCRIPTS/svg-visual-audit.mjs path/dir           # audits a specific dir
//   DRY_RUN=1 node SCRIPTS/svg-visual-audit.mjs          # report only, no edits
//   TOL=2 node SCRIPTS/svg-visual-audit.mjs              # overflow tolerance in px (default 2)
//
// Requires: ANTHROPIC_API_KEY in environment.
// Exit code: 0 if clean or all fixed, 2 if any SVG could not be fixed.
import { readdirSync, readFileSync, writeFileSync, statSync, existsSync } from 'fs';
import { join, basename } from 'path';
import { execSync } from 'child_process';
// Load keys from a single .env at the book root (gitignored). Real env wins.
for (const p of ['.env', '../.env']) {
  try {
    if (existsSync(p)) for (const line of readFileSync(p, 'utf8').split('\n')) {
      const m = line.match(/^\s*([A-Za-z0-9_]+)\s*=\s*(.*)\s*$/);
      if (m && !process.env[m[1]]) process.env[m[1]] = m[2].replace(/^['"]|['"]$/g, '');
    }
  } catch {}
}
const DIR     = process.argv[2] || 'images';
const TOL     = Number(process.env.TOL ?? 2);
const DRY_RUN = process.env.DRY_RUN === '1';
const API_KEY = process.env.ANTHROPIC_API_KEY;
if (!API_KEY && !DRY_RUN) { console.error('ANTHROPIC_API_KEY not set. Set it or run with DRY_RUN=1.'); process.exit(1); }
// ── character width estimator (for horizontal overflow) ─────────────────────
const NARROW = new Set("iIl.,:;'|!ftrj()[]-/ ");
const WIDE   = new Set("mwMW@");
const UPPER  = new Set("ABCDEFGHJKLNOPQRSTUVXYZ");
const charEm = c => NARROW.has(c) ? 0.30 : WIDE.has(c) ? 0.88 : UPPER.has(c) ? 0.66 : /[0-9]/.test(c) ? 0.55 : 0.52;
const textW  = (s, fs, ls = 0) => [...s].reduce((a, c) => a + charEm(c) * fs, 0) + Math.max(0, s.length - 1) * ls;
const num    = (v, d = 0) => { const n = parseFloat(String(v ?? '').replace(/[a-z%]+$/i, '')); return Number.isFinite(n) ? n : d; };
const attr   = (tag, name) => { const m = tag.match(new RegExp(`${name}\\s*=\\s*"([^"]*)"`)); return m ? m[1] : null; };
const decode = s => s.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#39;/g,"'");
function walk(dir) {
  let out = [];
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    if (statSync(p).isDirectory()) out = out.concat(walk(p));
    else if (e.toLowerCase().endsWith('.svg')) out.push(p);
  }
  return out;
}
// ── Phase 1: static heuristic scan ──────────────────────────────────────────
function staticScan(file) {
  const svg = readFileSync(file, 'utf8');
  const issues = [];
  // SUB: Unicode subscript digits in text content
  if (/[₀₁₂₃₄₅₆₇₈₉]/.test(svg))
    issues.push({ code: 'SUB', detail: 'Unicode subscript digits found — should use <tspan dy="0.3em" font-size="0.75em">' });
  // SUB: underscore notation like _n _i _0 inside text content
  const underscoreMatches = svg.match(/>([^<]*_[a-zA-Z0-9][^<]*)</g);
  if (underscoreMatches)
    issues.push({ code: 'SUB', detail: `Underscore subscript notation: ${underscoreMatches.slice(0,3).join(', ')}` });
  // SUP: Unicode superscript digits
  if (/[²³¹⁰⁴⁵⁶⁷⁸⁹⁺⁻]/.test(svg))
    issues.push({ code: 'SUP', detail: 'Unicode superscript characters found — should use <tspan dy="-0.5em" font-size="0.75em">' });
  // SUP: caret notation like ^2 ^n inside text content
  const caretMatches = svg.match(/>([^<]*\^[a-zA-Z0-9][^<]*)</g);
  if (caretMatches)
    issues.push({ code: 'SUP', detail: `Caret superscript notation: ${caretMatches.slice(0,3).join(', ')}` });
  // MATH: spelled-out Greek
  const greekSpelled = ['alpha','beta','gamma','delta','epsilon','theta','lambda','mu','sigma','omega','pi','phi','psi','rho'];
  for (const g of greekSpelled) {
    if (new RegExp(`>\\s*${g}\\s*[<\\s]`, 'i').test(svg))
      issues.push({ code: 'MATH', detail: `Greek letter "${g}" spelled out — should be the Unicode character` });
  }
  // MATH: arrow notation
  if (/>[^<]*->[^<]*</.test(svg))
    issues.push({ code: 'MATH', detail: '"-->" arrow notation found — should be →' });
  // MATH: not-equal notation
  if (/>[^<]*!=[^<]*</.test(svg))
    issues.push({ code: 'MATH', detail: '"!=" found — should be ≠' });
  // MATH: multiplication as asterisk
  if (/>[^<]*\*[^<]*</.test(svg))
    issues.push({ code: 'MATH', detail: '"*" used for multiplication — should be × or ·' });
  // OVER: geometry check
  const vb = (attr(svg.match(/<svg[^>]*>/i)?.[0] || '', 'viewBox') || '0 0 700 420').trim().split(/\s+/).map(Number);
  const [vw, vh] = [vb[2] || 700, vb[3] || 420];
  const rects = [];
  for (const m of svg.matchAll(/<rect\b[^>]*>/gi)) {
    const t = m[0], w = num(attr(t,'width')), h = num(attr(t,'height'));
    if (w > 0 && h > 0) rects.push({ x: num(attr(t,'x')), y: num(attr(t,'y')), w, h });
  }
  for (const m of svg.matchAll(/<text\b([^>]*)>([\s\S]*?)<\/text>/gi)) {
    const open = '<text ' + m[1] + '>';
    if (/transform\s*=/.test(open)) continue;
    const s = decode(m[2].replace(/<[^>]*>/g, '')).trim();
    if (!s) continue;
    const fs = num(attr(open,'font-size'), 12), x = num(attr(open,'x')), y = num(attr(open,'y'));
    const anchor = attr(open,'text-anchor') || 'start', ls = num(attr(open,'letter-spacing'));
    const w = textW(s, fs, ls);
    let left, right;
    if (anchor==='middle') { left=x-w/2; right=x+w/2; }
    else if (anchor==='end') { left=x-w; right=x; }
    else { left=x; right=x+w; }
    const bottom = y + fs * 0.22;
    const short = s.length > 44 ? s.slice(0,44)+'…' : s;
    if (right > vw + TOL)   issues.push({ code:'OVER', detail:`H-CANVAS '${short}' right=${right.toFixed(0)} > ${vw}` });
    if (bottom > vh + TOL)  issues.push({ code:'OVER', detail:`V-CANVAS '${short}' bottom=${bottom.toFixed(0)} > ${vh}` });
    let owner = null;
    for (const r of rects) {
      const insideX = x >= r.x-0.5 && x <= r.x+r.w+0.5;
      const insideY = y >= r.y-1 && y <= r.y+r.h+fs*0.35;
      if (insideX && insideY && (!owner || r.w*r.h < owner.w*owner.h)) owner=r;
    }
    if (owner) {
      const rb = owner.y+owner.h, rr = owner.x+owner.w;
      if (bottom > rb+TOL) issues.push({ code:'OVER', detail:`V-BOX '${short}' bottom=${bottom.toFixed(0)} > box=${rb.toFixed(0)} (+${(bottom-rb).toFixed(0)})` });
      if (right  > rr+TOL) issues.push({ code:'OVER', detail:`H-BOX '${short}' right=${right.toFixed(0)} > box=${rr.toFixed(0)} (+${(right-rr).toFixed(0)})` });
    }
  }
  return issues;
}
// ── Phase 2: AI fix ──────────────────────────────────────────────────────────
async function aiFixSVG(file, issues) {
  const svgSource = readFileSync(file, 'utf8');
  const issueList = issues.map(i => `[${i.code}] ${i.detail}`).join('\n');
  const prompt = `You are a precise SVG XML editor for mathematical and scientific textbook figures.
The following SVG has visual defects. Your job is to fix them and return the corrected SVG.
## Defects found by static analysis
${issueList}
## Fix rules (apply all that are relevant)
**SUB — subscript fixes**
- Replace Unicode subscript digits (₀₁₂…) with proper SVG: wrap the subscript character(s) in <tspan dy="0.3em" font-size="0.75em">n</tspan>, then reset with <tspan dy="-0.3em"> (empty, to restore baseline for following text)
- Replace underscore notation like "x_n" with: x<tspan dy="0.3em" font-size="0.75em">n</tspan>
- Ensure the subscript tspan is visibly smaller than body text
**SUP — superscript fixes**
- Replace Unicode superscript characters (²³…) with: <tspan dy="-0.5em" font-size="0.75em">n</tspan>, then reset with <tspan dy="0.5em">
- Replace caret notation like "x^2" with: x<tspan dy="-0.5em" font-size="0.75em">2</tspan>
**MATH — notation fixes**
- Spelled-out Greek: replace "alpha"→α, "beta"→β, "gamma"→γ, "delta"→δ, "epsilon"→ε, "theta"→θ, "lambda"→λ, "mu"→μ, "sigma"→σ, "omega"→ω, "pi"→π, "phi"→φ, "psi"→ψ, "rho"→ρ
- Arrow notation: replace "-->" or "->" with →
- Not-equal: replace "!=" with ≠
- Multiplication: replace bare "*" in formula context with × (U+00D7); in expression context use · (U+00B7)
**OVER — overflow fixes**
- V-BOX (text below its rect): increase that <rect>'s height attribute by (overflow_px + 8); if the rect is at the canvas bottom, increase the viewBox height instead
- H-BOX (text past right edge of rect): if room exists, increase rect width; else decrease font-size of that <text> by 1px
- H-CANVAS / V-CANVAS: split long captions into two <text> lines ~14px apart, or increase viewBox
**General constraints**
- Do not alter elements that are not involved in a flagged defect
- Preserve the book's visual design: colors, rx=0, stroke widths, font families
- Preserve valid XML throughout
- Do not add comments or explanations inside the SVG
## SVG to fix
${svgSource}
Return ONLY the corrected SVG XML, starting with <svg and ending with </svg>. No preamble, no markdown fences, no explanation.`;
  const resp = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-api-key': API_KEY, 'anthropic-version': '2023-06-01' },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 8192,
      messages: [{ role: 'user', content: prompt }]
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`API error ${resp.status}: ${err}`);
  }
  const data = await resp.json();
  const text = data.content.filter(b => b.type === 'text').map(b => b.text).join('');
  // strip any accidental markdown fences
  return text.replace(/^```[a-z]*\n?/i, '').replace(/\n?```$/, '').trim();
}
// ── Phase 3: re-render ────────────────────────────────────────────────────────
function rerender(svgPath) {
  const renderer = 'SCRIPTS/svg-to-png.mjs';
  if (!existsSync(renderer)) {
    console.log(`  [SKIP render] ${renderer} not found — PNG not updated`);
    return;
  }
  try {
    execSync(`node ${renderer} "${svgPath}"`, { stdio: 'inherit' });
  } catch (e) {
    console.error(`  [RENDER ERROR] ${e.message}`);
  }
}
// ── Main ─────────────────────────────────────────────────────────────────────
const files = walk(DIR).sort();
let total = files.length, flagged = 0, fixed = 0, failed = 0;
for (const f of files) {
  let issues;
  try { issues = staticScan(f); }
  catch (e) { console.log(`\n### ${f}\n  PARSE ERROR: ${e.message}`); failed++; continue; }
  if (!issues.length) continue;
  flagged++;
  const rel = f.replace(DIR + '/', '');
  console.log(`\n### ${rel}`);
  for (const i of issues) console.log(`  [${i.code}] ${i.detail}`);
  if (DRY_RUN) continue;
  process.stdout.write(`  → Requesting AI fix…`);
  try {
    const correctedSVG = await aiFixSVG(f, issues);
    if (!correctedSVG.startsWith('<svg') && !correctedSVG.startsWith('<?xml')) {
      throw new Error('AI response does not look like SVG');
    }
    writeFileSync(f, correctedSVG, 'utf8');
    console.log(' done. Re-rendering…');
    rerender(f);
    fixed++;
  } catch (e) {
    console.log(` FAILED: ${e.message}`);
    failed++;
  }
}
console.log(`\n==== ${flagged}/${total} SVGs flagged | ${fixed} fixed | ${failed} failed ====`);
if (DRY_RUN) console.log('DRY_RUN=1: no files were modified.');
console.log('Defect codes: SUB=subscript  SUP=superscript  MATH=notation  OVER=overflow');
process.exit(failed > 0 ? 2 : 0);
