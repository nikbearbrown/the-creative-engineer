# SaulBass.md
## Cowork Operations Guide: Mid-Century Symbolic Kindle Cover Generator

**Purpose**: This file governs all Kindle book cover generation in the mid-century cinematic poster style. Cowork reads this file before generating any SVG. Every cover produced by this system must pass all checklists in Section 8.

**Style label**: Do not describe output as "Saul Bass." Use: *mid-century modern cinematic poster design — cut-paper geometry, bold negative space, limited palette, symbolic abstraction, irregular hand-cut letterforms.*

**Cover text rule**: Kindle covers generated from this guide should show the book title only. Do not place author names, subtitles, series names, publisher names, taglines, blurbs, or footer text on the cover unless the user explicitly asks for them in the current request.

---

## 0. Input Schema

Every cover generation task begins with a populated JSON block. Do not proceed without it.

```json
{
  "title": "",
  "subtitle": "",
  "author": "",
  "subject_domain": "",
  "tone": "",
  "audience": "",
  "chapter_titles": [],
  "keywords": [],
  "avoid": [],
  "palette_preference": "",
  "series_name": "",
  "thumbnail_priority": "title and central icon"
}
```

**Required fields**: `title`, `subject_domain`, `chapter_titles`  
**Optional but improve output**: all others

---

## 1. Core Design Principle

> One concept. One tension. One symbol.

Do not illustrate the chapter content. Do not show literal subject matter. Extract the **central conflict** of the book and make one symbolic mark that embodies it.

| Book subject | Bad literal cover | Correct abstraction |
|---|---|---|
| Medicine | doctor, stethoscope | fragmented torso, missing organ shape, red slash |
| Mathematics | equations everywhere | geometric collision, triangle trapped in circle |
| AI ethics | robot face | black target shape inside a bureaucratic form |
| Social science | group photo | one figure separated from crowd silhouettes |
| Reliability engineering | circuit board | falling figure through broken red grid |
| Education | classroom scene | child-shape inside maze or grid |

---

## 2. Motif Selection Pipeline

Run this pipeline on every cover. Document the output before drawing anything.

### Step 1 — Extract central conflict

Read `title`, `subtitle`, and `chapter_titles`. Identify which of these conflicts the book is fundamentally about:

- human vs. system
- body vs. disease
- logic vs. uncertainty
- individual vs. institution
- signal vs. noise
- control vs. collapse
- pattern vs. chaos
- inside vs. outside
- part vs. whole

### Step 2 — Convert conflict to physical metaphor

| Conflict | Physical metaphor |
|---|---|
| control vs. collapse | falling figure, tower at tipping point |
| body vs. disease | fragmented torso, isolated organ, dissection lines |
| logic vs. uncertainty | broken grid, geometric shapes that almost align |
| individual vs. institution | tiny figure against massive wall or crowd |
| signal vs. noise | target with off-center mark, radiating bars |
| human vs. system | human silhouette assembled from rectangular blocks |
| pattern vs. chaos | grid dissolving at edges, spiral pulling inward |
| part vs. whole | fragments almost forming a complete shape, visible gaps |

### Step 3 — Select one motif from this list

| Motif | Use when |
|---|---|
| **Fragmented body** | medicine, psychology, diagnosis, identity, trauma, anatomy |
| **Falling figure** | finance, risk, ethics, safety, failure, crisis |
| **Spiral** | recursion, obsession, AI loops, psychology, addiction |
| **Broken grid** | mathematics, engineering, bureaucracy, systems |
| **Figure vs. crowd** | social science, politics, education, organizations |
| **Target / eye** | AI, surveillance, security, law, prediction |
| **Institutional wall** | policy, law, regulation, power structures |
| **Radiating bars** | discovery, alarm, revelation, media, politics |
| **Diagonal slash** | conflict, rupture, strategy, social change |
| **Figure in trap** | ethics, constraint, crisis, institutional capture |

**Rule**: Pick exactly one motif. Write it down. Do not combine motifs.

---

## 3. Color System

Use exactly **3 colors**: background + figure + accent. No fourth color. No gradient. No shadow. No texture (unless paper grain is extremely subtle).

**Canvas base note**: The warmest, most authentic mid-century feel comes from ivory/cream backgrounds rather than stark white. These replicate the flat, tactile quality of silkscreen printing on paper stock.

| Palette name | Background | Figure | Accent | Use for |
|---|---|---|---|---|
| **Silkscreen Ivory** | `#F4EFEB` | `#111111` | `#D32F2F` | default academic, most authentic mid-century feel |
| **Ochre Cream** | `#F1E9D2` | `#111111` | `#D32F2F` | warmer alternative; crime, espionage, history |
| **Academic serious** | `#E8D8B8` | `#111111` | `#B63A2B` | general academic, serious tone |
| **Medical danger** | `#F2E7D5` | `#101010` | `#C6342E` | medicine, biology, pathology |
| **Bass Red** | `#D62B2B` | `#F5F0E8` | `#111111` | urgency, drama, law, crisis |
| **Bass Gold** | `#F5C518` | `#111111` | `#D62B2B` | warning, math, physics, economics |
| **Bass Teal** | `#1B6B5A` | `#F5F0E8` | `#F5C518` | science, biology, CS, engineering |
| **Bass Navy** | `#1C2B4A` | `#F5F0E8` | `#D62B2B` | social science, history, political science |
| **Bass Charcoal** | `#2B2B2B` | `#F5F0E8` | `#F5C518` | philosophy, psychology, writing |
| **Bass Orange** | `#E8621A` | `#111111` | `#F5F0E8` | chemistry, technology, engineering |
| **Tech / Math** | `#111111` | `#F4EFEB` | `#1565C0` | high-contrast; dark field = logic/space |
| **History / Politics** | `#F4EFEB` | `#111111` | `#EF6C00` | orange commands focus at thumbnail size |
| **Noir / legal** | `#D8D0C0` | `#0D0D0D` | `#A62626` | law, crime, ethics, noir |
| **Children / learning** | `#F6D24A` | `#191919` | `#E85B3A` | education, children, playful |

**Distribution rules**:
- Background: 60–70% of canvas area
- Figure color: 20–30%
- Accent: ≤15% (one element only — either type emphasis or one compositional fragment)
- Negative space (bare background): minimum 40% of total canvas

### Penguin Genre-Color Reference

When subject domain maps ambiguously to a palette, use this secondary signal (Penguin Books, 1935 — the closest historical parallel to systematic academic cover coding):

| Genre | Color | Hex |
|---|---|---|
| General fiction | Orange | `#FF6600` |
| Crime / mystery | Green | `#008000` |
| Biography / memoir | Dark blue | `#000080` |
| Drama / plays | Red | `#FF0000` |
| Essays / criticism | Purple | `#800080` |
| World affairs / politics | Grey | `#808080` |

---

## 4. SVG Canvas Rules

### Viewport

```xml
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 1600 2560" 
     width="100%" 
     height="100%"
     preserveAspectRatio="xMidYMid meet"
     shape-rendering="geometricPrecision">
```

**Portrait only.** Do not use 2560×1600. Kindle covers are portrait: 1600 wide × 2560 tall.

`shape-rendering="geometricPrecision"` ensures the rasterizer calculates shape boundaries with maximum precision, keeping flat-color edges crisp. For elements made entirely of vertical and horizontal blocks, you may additionally set `shape-rendering="crispEdges"` on specific nodes to disable anti-aliasing entirely — useful for grid-based motifs.

### Safe Zones

```
Outer margin (no important content):    80 px all sides
Title safe zone (x):                    120–1480
Top safe zone (y):                      120–900
Main visual zone (y):                   700–1900
Lower negative-space zone (y):         2150–2420
```

### Compositional Zones (default layout)

```
Zone A — Figure area:     y: 200–1400   (primary symbolic element)
Zone B — Title area:      y: 1400–2200  (large typographic element)
Zone C — Breathing room:   y: 2200–2460  (usually empty; no author/footer text)
```

Breaking this zone order is allowed when the motif demands it (e.g., figure bleeding into title zone).

### Layer Order (SVG group structure)

```xml
<g id="background">...</g>
<g id="symbol-fragments">...</g>
<g id="accent-elements">...</g>
<g id="title-letterforms">...</g>
```

---

## 5. Figure Construction Rules

### Shape primitives

Use `<polygon>`, `<path>`, and `<rect>` only for primary forms.  
Do **not** use `<circle>` for heads or primary shapes — circles are too smooth and finished.  
Use 5–8 vertex polygons for "organic-geometric" forms that feel hand-cut.

### Human figure abstraction

```xml
<!-- Head: irregular hexagon, NOT circle -->
<polygon points="780,280 820,260 860,270 870,320 840,350 790,345 760,320" 
         fill="#111111"/>

<!-- Torso: trapezoid -->
<polygon points="750,360 850,360 870,580 730,580" fill="#111111"/>

<!-- Fragmented arm: floats separate from torso — gap is intentional -->
<polygon points="600,380 650,370 680,420 670,460 620,450 590,410" 
         fill="#111111"/>
```

### Fragmentation rules

- Use 5–9 fragments; not dozens
- Fragments should *almost* align into a whole figure but not quite
- Leave visible gaps — the negative space is the wound
- Avoid any sense of realistic gore — keep it flat and symbolic
- One fragment may become a typographic container (a word inside a body part)

### Rotation rule

Rotate the primary figure group 5–15 degrees off vertical. This single change creates kinetic tension.

```xml
<g transform="rotate(-8, 800, 1280)">
  <!-- all figure elements here -->
</g>
```

### Negative space rule

At least **40% of the canvas** must remain as bare background color. Concentrate visual mass in one diagonal band or corner. Do not fill the canvas evenly.

---

## 6. Typography Rules

### Size minimums (at 1600×2560 canvas)

| Element | SVG font-size |
|---|---|
| Main title | 160–280 px |
| Subtitle | Do not include unless explicitly requested |
| Author | Do not include unless explicitly requested |
| Series / label | Do not include unless explicitly requested |
| Anything smaller | Do not include |

### Font

Use `font-family="Arial Black, Arial, sans-serif"` for portability across renderers. Convert to paths in final export.

### Word-breaking (Bass style)

Break compound or conceptually divisible words across lines to create visual rhythm:

```
Good breaks:          Bad breaks:
ANATO / MY            THE / BOOK / OF
RELI / ABILITY        INTRO / DUCTION
SOCIO / LOGY          BASIC / IDEAS
ALGO / RITHM
DIS / ORDER
```

**Rule**: break only words where the break adds meaning or improves visual rhythm. Never break short words. Never break the title into fragments that are unreadable at 100 px.

### Type-image fusion

The title must not sit politely above an illustration. It must interact with the figure:

- Put one word inside a body fragment
- Let a diagonal slash split the title
- Stack the title as a block that forms a wall the figure pushes against
- Let the image interrupt or overlap with letters
- Replace one letter with a symbolic shape (the `O` in SOCIOLOGY becomes a target)

### All-caps

Use all-caps for the visible title. By default, the title is the only text on the cover.

---

## 7. SVG Template Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 2560" 
     width="1600" height="2560">
  
  <!-- BACKGROUND -->
  <rect width="1600" height="2560" fill="#1B6B5A"/>
  
  <!-- FIGURE — rotated for kinetic tension -->
  <g id="symbol-fragments" transform="rotate(-8, 800, 900)">
    
    <!-- Head: irregular polygon -->
    <polygon points="780,280 825,258 868,272 875,328 842,354 788,348 758,318" 
             fill="#F5F0E8"/>
    
    <!-- Torso -->
    <polygon points="740,368 860,368 878,590 722,590" fill="#F5F0E8"/>
    
    <!-- Left arm — intentional gap from torso -->
    <polygon points="592,385 648,372 678,428 665,468 608,455 582,415" 
             fill="#F5F0E8"/>
    
    <!-- Right arm — floating -->
    <polygon points="888,375 944,388 958,445 932,470 876,452 862,408" 
             fill="#F5F0E8"/>
    
    <!-- Left leg -->
    <polygon points="730,598 790,598 778,820 718,812" fill="#F5F0E8"/>
    
    <!-- Right leg — offset for asymmetry -->
    <polygon points="808,598 868,598 882,835 822,840" fill="#F5F0E8"/>
    
  </g>
  
  <!-- ACCENT ELEMENT (≤15% of canvas) -->
  <rect x="0" y="1350" width="1600" height="18" fill="#F5C518"/>
  
  <!-- TITLE BLOCK -->
  <text x="80" y="1540" 
        font-family="Arial Black, Arial, sans-serif"
        font-size="240" font-weight="900"
        fill="#F5F0E8" letter-spacing="-4">
    INTRO
  </text>
  <text x="80" y="1800"
        font-family="Arial Black, Arial, sans-serif" 
        font-size="240" font-weight="900"
        fill="#F5C518" letter-spacing="-4">
    TO
  </text>
  <text x="80" y="2060"
        font-family="Arial Black, Arial, sans-serif"
        font-size="200" font-weight="900"
        fill="#F5F0E8" letter-spacing="-3">
    BIOLOGY
  </text>
</svg>
```

---

## 8. Conversion Pipeline

### Primary: Node.js + sharp (recommended — batch-compatible)

```javascript
const sharp = require('sharp');
const fs = require('fs');

async function svgToKindleCover(svgPath, outputPath) {
  const svgBuffer = fs.readFileSync(svgPath);
  
  await sharp(svgBuffer, { density: 300 })
    .resize(1600, 2560, {
      fit: 'fill',
      kernel: sharp.kernel.lanczos3
    })
    .flatten({ background: { r: 244, g: 239, b: 235 } })  // flatten transparency to ivory
    .jpeg({
      quality: 92,
      chromaSubsampling: '4:4:4',
      mozjpeg: true
    })
    .toFile(outputPath);
}

svgToKindleCover('./cover.svg', './cover.jpg');
```

**Note on `.flatten()`**: SVG backgrounds are technically transparent until filled. The `.flatten()` call ensures any transparent layers composite against the canvas base color rather than black. Match the background value to your chosen palette's background hex.

### Fallback: Inkscape + ImageMagick (highest fidelity, slower)

```bash
# Step 1: SVG to PNG at 2× for oversampling
inkscape cover.svg \
  --export-type=png \
  --export-filename=cover_2x.png \
  --export-width=3200 \
  --export-height=5120

# Step 2: Downsample PNG to final size
magick cover_2x.png \
  -resize 1600x2560 \
  -background "#F4EFEB" \
  -alpha remove \
  -colorspace sRGB \
  -quality 92 \
  -strip \
  cover.jpg
```

### Fallback: ImageMagick direct (use only if environment is stable)

```bash
# -density 1200 forces high-res SVG input before downscaling — prevents blur
magick -density 1200 \
       -background "#F4EFEB" \
       cover.svg \
       -resize 1600x2560 \
       -alpha remove \
       -colorspace sRGB \
       -quality 92 \
       -strip cover.jpg
```

**Warning**: ImageMagick's default SVG renderer (MSVG) is unreliable for modern SVG. Use Inkscape or sharp/librsvg pipelines for production.

### Fallback: rsvg-convert (Linux/server)

```bash
rsvg-convert --width=1600 --height=2560 \
             --background-color="#F4EFEB" \
             cover.svg > cover.png
magick cover.png -colorspace sRGB -quality 92 -strip cover.jpg
```

### Thumbnail test

```bash
magick cover.jpg -resize 100x160 cover_thumb.jpg
```

---

## 9. Checklists

### Design checklist (run before generating SVG)

- [ ] Central conflict identified and written down
- [ ] One motif selected from Section 2 — only one
- [ ] Palette selected from Section 3 — exactly 3 colors
- [ ] Figure constructed from polygons/paths/rects — no circles as primary forms
- [ ] Figure rotated 5–15 degrees off vertical
- [ ] Fragmentation present — gaps visible
- [ ] Negative space ≥ 40% of canvas
- [ ] Title breaks at syllable/concept boundaries if longer than 8 letters
- [ ] Type and figure interact — they are not in separate zones
- [ ] Visible cover text is title-only unless the user explicitly requested additional text

### Technical checklist (run before KDP upload)

- [ ] SVG root has `shape-rendering="geometricPrecision"` and `preserveAspectRatio="xMidYMid meet"`
- [ ] SVG viewBox is `0 0 1600 2560`
- [ ] Final output is JPG
- [ ] File size under 5 MB (strict KDP limit; target 1–2 MB)
- [ ] Color space is sRGB
- [ ] No external images or fonts referenced
- [ ] Text converted to paths in final export SVG
- [ ] Nothing important within 80 px of any edge
- [ ] `.flatten()` applied in sharp pipeline to handle transparency

### Thumbnail test (pass criteria at 100×160 px)

- [ ] Main title or first title word is legible (OCR confidence >90% if automated)
- [ ] Central symbol shape is recognizable
- [ ] Luminosity contrast ratio between figure and background >4.5:1
- [ ] Total independent `<path>` node count <15 in the SVG (more = thumbnail collapse into noise)
- [ ] No subtitle, author, series, publisher, blurb, or footer text is present unless explicitly requested
- [ ] Cover distinguishable from a generic abstract rectangle

**If thumbnail fails**:
- OCR below 90% → increase title font-size by 15% and regenerate
- Contrast below 4.5:1 → swap higher-contrast palette or widen gaps between fragments
- Path count above 15 → merge adjacent paths, prune any detail under 20px

---

## 10. Programmatic Generation Schema

For automated batch generation, structure each cover as a layout graph. The LLM selects the metaphor and parameters; deterministic code draws the SVG.

```json
{
  "cover": {
    "canvas": { "width": 1600, "height": 2560 },
    "style": "mid-century symbolic cut-paper",
    "palette": {
      "background": "#1B6B5A",
      "foreground": "#F5F0E8",
      "accent": "#F5C518"
    },
    "motif": {
      "type": "fragmented_body",
      "rotation_degrees": -8,
      "fragment_count": 7,
      "fragment_gap_px": 12,
      "symbol_y_range": [200, 1400]
    },
    "typography": {
      "title_words": ["INTRO", "TO", "BIOLOGY"],
      "title_y_positions": [1540, 1800, 2060],
      "title_sizes": [240, 240, 200],
      "title_accent_word_index": 1,
      "visible_text_policy": "title_only"
    },
    "accent_bar": {
      "x": 0, "y": 1350, "width": 1600, "height": 18
    },
    "export": {
      "svg_source": "cover.svg",
      "jpg_output": "cover.jpg",
      "width": 1600,
      "height": 2560,
      "quality": 92,
      "colorspace": "sRGB"
    }
  }
}
```

---

## 11. Claude System Prompt (for SVG generation step)

Use this when calling Claude to generate the SVG from populated inputs:

```
You generate SVG book covers using mid-century modern cinematic poster design vocabulary:
symbolic abstraction, cut-paper geometry, bold negative space, limited palette,
irregular hand-cut letterforms, and strong title-image integration.

Do not reproduce any specific existing poster. Create original compositions.

Rules you must follow:
- Output valid SVG only. Start with <svg and end with </svg>. No markdown fences.
- Canvas: viewBox="0 0 1600 2560" width="1600" height="2560"
- Flat vector shapes only. No raster images. No external fonts. No drop shadows.
- No gradients unless extremely subtle (prefer none).
- Exactly 3 colors: background, figure, accent.
- Background covers ≥60% of canvas. Negative space ≥40%.
- Build figures from <polygon>, <path>, <rect> — no <circle> for primary forms.
- Rotate primary figure group 5–15 degrees off vertical.
- Fragment the figure: intentional gaps between parts.
- Title at 160–280px, all caps, interacts physically with figure.
- The title is the only visible text. Do not include author, subtitle, series, publisher, blurb, or footer text unless the user explicitly requests it.
- Use font-family="Arial Black, Arial, sans-serif"
- Design must read at 100px thumbnail.
- Before drawing, state: (1) central conflict, (2) selected motif, (3) selected palette.
  Then output SVG.
```

---

## 12. Subject → Motif Quick Reference

| Subject | Conflict | Motif | Palette |
|---|---|---|---|
| Medicine / Biology | body under stress | Fragmented body | Medical danger |
| Cancer / Pathology | growth vs. containment | Form breaking boundary | Bass Red |
| Mathematics | order vs. infinity | Broken grid | Bass Gold |
| Physics | force acting on matter | Falling figure | Bass Charcoal |
| Chemistry | bonding and breaking | Connected nodes, one severed | Bass Orange |
| Computer Science | human vs. machine | Figure made of rectangular blocks | Bass Teal |
| AI / Machine Learning | pattern vs. noise | Grid with one anomaly, target | Bass Navy |
| Social Science | individual vs. collective | Figure vs. crowd | Academic serious |
| Psychology | interior vs. exterior | Figure with visible internal structure | Bass Charcoal |
| Political Science | power vs. opposition | Two asymmetric figures | Bass Navy |
| Economics | scarcity vs. distribution | Unequal divisions of rectangle | Bass Gold |
| Law | judgment under uncertainty | Figure caught between two forces | Noir / legal |
| History | past acting on present | Layered overlapping figures | Academic serious |
| Writing / Language | meaning constructed from parts | Letters fragmented and reassembled | Bass Charcoal |
| Engineering | structure under load | Arch at maximum stress | Bass Orange |
| Reliability / Ops | control vs. collapse | Falling figure, broken grid | Bass Red |
| Education | individual in system | Child-figure inside maze or grid | Children / learning |

---

## 13. SCRIPTS/generate-cover.mjs — Full Pipeline

### What it does

1. Reads `metadata.yaml` from the book root
2. If `subject_domain`, `tone`, `keywords`, or `chapter_titles` are empty, reads all `chapters/*.md` files and calls the Claude API to infer them, then **writes the inferred values back into `metadata.yaml`**
3. Calls the Claude API with the Section 11 system prompt + populated metadata to generate the SVG
4. Writes `cover.svg` to the book root
5. Converts `cover.svg` → `cover.jpg` via sharp (1600×2560, quality 92, flatten to palette background)
6. Runs the thumbnail test: exports `cover_thumb.jpg` at 100×160
7. Logs what was inferred and what was generated

### Location

Lives in `bear-textbooks/SCRIPTS/generate-cover.mjs` alongside `enrich-books.mjs`.  
`SaulBass.md` lives in `bear-textbooks/brutalist/SaulBass.md` alongside `CLAUDE.md`, `DESIGN.md`, `PROJECT.md`, `VIZ.md`.

### Usage

```bash
# From bear-textbooks root:
node SCRIPTS/generate-cover.mjs books/quantum-mechanics-1

# Dry run — infer and update metadata.yaml but stop before SVG generation:
node SCRIPTS/generate-cover.mjs books/quantum-mechanics-1 --infer-only

# Skip inference — use metadata.yaml as-is even if fields are empty:
node SCRIPTS/generate-cover.mjs books/quantum-mechanics-1 --no-infer

# Regenerate SVG without re-running inference:
node SCRIPTS/generate-cover.mjs books/quantum-mechanics-1 --no-infer --force
```

### Phase 1 — Metadata inference

When any of `subject_domain`, `tone`, `keywords`, `chapter_titles` are missing or empty arrays, the script:

1. Reads every file in `chapters/` (skipping `00-frontmatter.md` and `99-back-matter.md`)
2. Extracts: all `# Heading` lines, the first paragraph of each chapter, and any `<!-- → [TYPE: ...]-->` figure comments
3. Sends that digest + the book title/subtitle/author to Claude with this inference prompt:

```
You are analyzing a book manuscript to extract metadata for cover design.

Given the book title, subtitle, and chapter content digest below, return ONLY
a JSON object with these fields:

{
  "subject_domain": "one of: medicine, biology, physics, chemistry, mathematics, 
    computer_science, ai_ml, social_science, psychology, political_science, 
    economics, law, history, writing, engineering, reliability, education, 
    quantum_mechanics, other",
  "tone": "one of: serious, urgent, playful, technical, clinical, accessible",
  "keywords": ["array", "of", "5-10", "thematic", "keywords"],
  "chapter_titles": ["array of actual chapter titles found in the content"]
}

Return only the JSON object. No explanation, no markdown fences.

BOOK TITLE: {{title}}
SUBTITLE: {{subtitle}}
AUTHOR: {{author}}

CHAPTER DIGEST:
{{digest}}
```

4. Merges the returned values into `metadata.yaml`, preserving any fields that were already populated
5. Logs each inferred field clearly: `[inferred] subject_domain: quantum_mechanics`

### Phase 2 — SVG generation

Sends the fully populated metadata to Claude with the Section 11 system prompt. The user prompt is:

```
Generate a mid-century symbolic cut-paper SVG book cover.

TITLE: {{title}}
SUBTITLE: {{subtitle}}
AUTHOR: {{author}}
SUBJECT DOMAIN: {{subject_domain}}
TONE: {{tone}}
AUDIENCE: {{audience}}
KEYWORDS: {{keywords}}
CHAPTER TITLES:
{{chapter_titles}}

Canvas: 1600 × 2560px portrait.
Output raw SVG only. No markdown. No explanation.
```

Writes the raw SVG response to `cover.svg`.

### Phase 3 — Conversion and thumbnail

```javascript
// Convert SVG → JPG
await sharp(svgBuffer, { density: 300 })
  .resize(1600, 2560, { fit: 'fill', kernel: sharp.kernel.lanczos3 })
  .flatten({ background: { r: 244, g: 239, b: 235 } })
  .jpeg({ quality: 92, chromaSubsampling: '4:4:4', mozjpeg: true })
  .toFile('cover.jpg');

// Thumbnail test
await sharp('cover.jpg')
  .resize(100, 160)
  .toFile('cover_thumb.jpg');
```

Logs: `✓ cover.jpg written (1600×2560)` and `✓ cover_thumb.jpg written — inspect before upload`

### Dependencies

`sharp` is already installed. Only `js-yaml` is new:

```bash
npm install js-yaml
```

No changes to `new_book.py` needed — the script lives at the repo level, not per-book.
