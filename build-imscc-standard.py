#!/usr/bin/env python3
"""build-imscc-standard.py — portable IMS Common Cartridge 1.3 builder.

Reads the same source that produces the EPUB (chapters/*.md + metadata.yaml)
and compiles a .imscc course package that imports into Canvas, Moodle,
Blackboard, and Brightspace.

Standard library only — nothing to install, nothing to break.

  python3 build-imscc-standard.py
  python3 build-imscc-standard.py --out output/ai1-cli.imscc
  python3 build-imscc-standard.py --source-dir . --blueprint BLUEPRINT.md   (--tiktoc still accepted)

It does NOT write the Canvas-flavored trigger files (course_settings/*) — that
is the optional Canvas-optimized path. This produces portable Common Cartridge.
"""
import argparse
import html
import os
import re
import sys
import uuid
import zipfile
from xml.sax.saxutils import escape as xml_escape

CC_NS = "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1"
LOM_MAN = "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/manifest"
XSI = "http://www.w3.org/2001/XMLSchema-instance"
SCHEMALOC = (
    "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1 "
    "http://www.imsglobal.org/profile/cc/ccv1p3/ccv1p3_imscp_v1p2_v1p0.xsd "
    + LOM_MAN +
    " http://www.imsglobal.org/profile/cc/ccv1p3/LOM/ccv1p3_lommanifest_v1p0.xsd"
)


def uid(prefix="i"):
    return prefix + uuid.uuid4().hex


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "untitled"


def read_metadata(source_dir):
    """Minimal YAML read — we only need a few top-level scalar keys."""
    meta = {"title": "Untitled", "author": "", "language": "en-US"}
    path = os.path.join(source_dir, "metadata.yaml")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^\s*(title|author|language)\s*:\s*(.+?)\s*$", line)
                if m:
                    key, val = m.group(1), m.group(2).strip().strip('"').strip("'")
                    if val:
                        meta[key] = val
    return meta


# ── markdown → HTML (stdlib, serviceable subset) ────────────────────────────
_INLINE_CODE = re.compile(r"`([^`]+)`")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC = re.compile(r"(?<![\*\w])\*([^*]+)\*(?![\*\w])")
_IMG = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _inline(text):
    """Escape HTML, then apply inline markdown. Code spans are protected."""
    spans = []

    def stash(m):
        spans.append(html.escape(m.group(1)))
        return "\x00%d\x00" % (len(spans) - 1)

    text = _INLINE_CODE.sub(stash, text)
    text = html.escape(text)
    text = _IMG.sub(lambda m: '<img src="%s" alt="%s" />' % (m.group(2), html.escape(m.group(1))), text)
    text = _LINK.sub(lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), text)
    text = _BOLD.sub(r"<strong>\1</strong>", text)
    text = _ITALIC.sub(r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % spans[int(m.group(1))], text)
    return text


def md_to_html(md):
    out = []
    lines = md.split("\n")
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]

        # raw HTML comment block (e.g. <!-- → [TABLE: ...] -->) — pass through, stays invisible
        if line.lstrip().startswith("<!--"):
            block = [line]
            while "-->" not in line and i + 1 < n:
                i += 1
                line = lines[i]
                block.append(line)
            out.append("\n".join(block))
            i += 1
            continue

        # fenced code
        if line.startswith("```"):
            code = []
            i += 1
            while i < n and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(code)))
            continue

        # blank
        if not line.strip():
            i += 1
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, _inline(m.group(2)), lvl))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^(\*{3,}|-{3,}|_{3,})\s*$", line):
            out.append("<hr />")
            i += 1
            continue

        # table (pipe). header row + separator row of ---|---
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i + 1]):
            def cells(row):
                row = row.strip().strip("|")
                return [c.strip() for c in row.split("|")]
            header = cells(line)
            i += 2
            body = []
            while i < n and "|" in lines[i] and lines[i].strip():
                body.append(cells(lines[i]))
                i += 1
            t = ["<table>", "<thead><tr>"]
            t += ["<th>%s</th>" % _inline(c) for c in header]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join("<td>%s</td>" % _inline(c) for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        # blockquote
        if line.lstrip().startswith(">"):
            quote = []
            while i < n and lines[i].lstrip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>%s</blockquote>" % _inline(" ".join(quote)))
            continue

        # unordered list
        if re.match(r"^\s*[-*+]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*+]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*+]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join("<li>%s</li>" % _inline(it) for it in items) + "</ul>")
            continue

        # ordered list
        if re.match(r"^\s*\d+[.)]\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+[.)]\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+[.)]\s+", "", lines[i]))
                i += 1
            out.append("<ol>" + "".join("<li>%s</li>" % _inline(it) for it in items) + "</ol>")
            continue

        # paragraph (gather until blank)
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|\s*[-*+]\s|\s*\d+[.)]\s|>)", lines[i]):
            para.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % _inline(" ".join(para)))
    return "\n".join(out)


def page_html(title, body_html, lang="en-US"):
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html lang="%s"><head><meta charset="utf-8" />\n'
        "<title>%s</title></head>\n<body>\n%s\n</body></html>\n"
        % (lang, html.escape(title), body_html)
    )


# ── chapter model ───────────────────────────────────────────────────────────
EXERCISE_HEADING = re.compile(r"^##\s+(.*\b(?:LLM\s+)?Exercises?\b.*)$", re.IGNORECASE | re.MULTILINE)


def first_title(md, fallback):
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def split_exercises(md):
    """Return (main_md, exercises_md|None). Exercises = from its ## heading to the next ## heading."""
    m = EXERCISE_HEADING.search(md)
    if not m:
        return md, None
    start = m.start()
    nxt = re.search(r"^##\s+", md[m.end():], re.MULTILINE)
    end = m.end() + nxt.start() if nxt else len(md)
    return md[:start] + md[end:], md[start:end]


def classify(fname):
    n = fname.lower()
    if "appendix" in n:
        return "appendix"
    if "back-matter" in n or n.startswith("99"):
        return "back"
    if "frontmatter" in n or "front-matter" in n:
        return "front"
    return "chapter"


def main():
    ap = argparse.ArgumentParser(description="Build a portable IMS Common Cartridge 1.3 (.imscc).")
    ap.add_argument("--source-dir", default=".", help="book root with chapters/ and metadata.yaml")
    ap.add_argument("--out", default=None, help="output .imscc path")
    ap.add_argument("--blueprint", "--tiktoc", dest="tiktoc", default=None,
                    help="optional BLUEPRINT.md (formerly TIKTOC.md; confirms module order)")
    args = ap.parse_args()

    src = args.source_dir
    chapters_dir = os.path.join(src, "chapters")
    if not os.path.isdir(chapters_dir):
        sys.exit("No chapters/ found in %s" % os.path.abspath(src))

    meta = read_metadata(src)
    title = meta["title"]
    lang = meta.get("language", "en-US")
    out_path = args.out or os.path.join(src, "output", slugify(title) + ".imscc")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    files = sorted(f for f in os.listdir(chapters_dir) if f.endswith(".md"))

    # buckets
    front, chapter_mods, appendices, back = [], [], [], []
    resources = []   # (identifier, href, html_string)
    page_count = 0

    def add_page(item_title, md, stem, suffix=""):
        nonlocal page_count
        body = md_to_html(md)
        rid = uid("r")
        href = "web_resources/%s%s.html" % (stem, suffix)
        resources.append((rid, href, page_html(item_title, body, lang)))
        page_count += 1
        return {"id": uid("item"), "title": item_title, "ref": rid}

    for f in files:
        stem = f[:-3]
        with open(os.path.join(chapters_dir, f), encoding="utf-8") as fh:
            md = fh.read()
        kind = classify(f)
        t = first_title(md, stem)
        main_md, ex_md = split_exercises(md)
        items = [add_page(t, main_md, stem)]
        if ex_md:
            items.append(add_page(t + " — Exercises", ex_md, stem, "-exercises"))
        entry = {"title": t, "items": items}
        if kind == "front":
            front.extend(items)
        elif kind == "appendix":
            appendices.extend(items)
        elif kind == "back":
            back.extend(items)
        else:
            chapter_mods.append(entry)

    # organization tree
    modules = []
    if front:
        modules.append(("Start Here", front))
    for ch in chapter_mods:
        modules.append((ch["title"], ch["items"]))
    if appendices:
        modules.append(("Appendices", appendices))
    if back:
        modules.append(("Back Matter", back))

    # build manifest
    def item_xml(it):
        return ('      <item identifier="%s" identifierref="%s"><title>%s</title></item>'
                % (it["id"], it["ref"], xml_escape(it["title"])))

    org_items = []
    for mod_title, items in modules:
        kids = "\n".join(item_xml(it) for it in items)
        org_items.append(
            '    <item identifier="%s"><title>%s</title>\n%s\n    </item>'
            % (uid("mod"), xml_escape(mod_title), kids)
        )
    res_xml = "\n".join(
        '    <resource identifier="%s" type="webcontent" href="%s">\n'
        '      <file href="%s"/>\n    </resource>' % (rid, href, href)
        for rid, href, _ in resources
    )

    manifest = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<manifest identifier="%s"\n'
        '    xmlns="%s"\n    xmlns:lomimscc="%s"\n    xmlns:xsi="%s"\n'
        '    xsi:schemaLocation="%s">\n'
        '  <metadata>\n    <schema>IMS Common Cartridge</schema>\n'
        '    <schemaversion>1.3.0</schemaversion>\n'
        '    <lomimscc:lom><lomimscc:general><lomimscc:title>'
        '<lomimscc:string>%s</lomimscc:string></lomimscc:title></lomimscc:general></lomimscc:lom>\n'
        '  </metadata>\n'
        '  <organizations>\n    <organization identifier="%s" structure="rooted-hierarchy">\n'
        '      <item identifier="%s">\n%s\n      </item>\n'
        '    </organization>\n  </organizations>\n'
        '  <resources>\n%s\n  </resources>\n</manifest>\n'
        % (uid("M"), CC_NS, LOM_MAN, XSI, SCHEMALOC, xml_escape(title),
           uid("org"), uid("root"),
           "\n".join("  " + l for l in "\n".join(org_items).split("\n")),
           res_xml)
    )

    # write zip
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest)
        for _, href, html_str in resources:
            z.writestr(href, html_str)

    print("Built: %s" % out_path)
    print("  course title : %s" % title)
    print("  modules      : %d" % len(modules))
    print("  web pages    : %d" % page_count)
    print("  manifest     : imsmanifest.xml (Common Cartridge 1.3.0)")


if __name__ == "__main__":
    main()
