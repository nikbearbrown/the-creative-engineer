# VIZ.md - Data Visualization Constitution
NEU Northeastern
*Northeastern University Brand + Effective Data Visualization. Load on-demand before any Generate phase session that touches charts, dashboards, D3, SVG data graphics, statistical figures, maps, networks, or interactive visual analysis.*
*Updated: May 2026 · Load status: on-demand (data visualization sessions only)*

---

## Relationship to the governing files

`CLAUDE.md` governs D3 code: version, naming, joins, accessibility implementation, data loading, and runtime behavior.

`DESIGN.md` governs the visual brand: palette, typography, spacing, dark mode, surfaces, component rules, and what the Northeastern system never does.

`VIZ.md` governs data visualization: chart selection, marks and channels, perceptual honesty, graph-specific rules, chart-family constraints, and the verification checklist for effective graphs.

When files conflict:
- `DESIGN.md` wins on brand, color tokens, typography, spacing, and surface rules.
- `CLAUDE.md` wins on D3 syntax, file structure, and implementation patterns.
- `VIZ.md` wins on chart choice, data encoding, channel assignment, perceptual accuracy, and data visualization audit rules.

---

## Governing principle

Every mark earns its presence by serving the communication question. The chart follows the reader's task, not the shape of the spreadsheet. Position and length carry quantitative truth; color supports, annotates, and directs. Northeastern red is the primary series and brand accent, not a generic warning color. Gold is a decorative note, not a data channel.

If the chart does not let a reader answer the intended question faster, more accurately, and with less ambiguity than a table, the chart is not finished.

---

## Phase model for visualization work

### Phase A - Audit

Before generating a chart, read the data.

Required audit:
- List every field and classify it as categorical, ordinal, quantitative, temporal, geographic, hierarchical, network, or text.
- State the unit of observation.
- State the denominator for every rate, percentage, index, or normalized value.
- Identify missing values, censored values, outliers, and transformations.
- Name whether values are counts, rates, ranks, shares, indices, logs, residuals, estimates, or forecasts.
- Write the reader question in one sentence.
- Ask Cairo's question: compared with what?
- Decide whether the task is comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial, or specialized.

No chart is generated until the audit exists.

### Phase B - Schema

Before writing code, specify the chart.

Required schema:
- Chart type and why it fits the reader question.
- Mark types: point, line, area, glyph, polygon, node, link, or text.
- Channel-to-attribute mapping for every encoded variable.
- Sort order and grouping logic.
- Scale type for every quantitative channel.
- Domain limits, zero-baseline decisions, and log-scale decisions.
- Color role and palette token for every series.
- Accessibility decisions: title, description, focus behavior, tooltip, direct labels, and color-blind support.

### Phase C - Generate

Generate one chart or one chart component per prompt. Do not combine chart selection, data cleaning, interaction design, and visual styling into one request unless the schema is already complete.

Claude Code is the right labor for D3 implementation, scale construction, joins, axis rendering, layout algorithms, responsive redraws, tooltips, accessibility metadata, and small interaction states.

The human is the right labor for the communication question, chart type, ethical framing, encoding trade-offs, causal claims, and the final decision that the chart works.

### Phase D - Verify

Open the chart in a browser. Read the chart against the data and the schema. Resize it. Test dark mode if required. Test keyboard focus and reduced motion. Audit color usage, axis choices, and annotations.

### Phase E - Handoff

Ship with data source notes, transformation notes, chart type rationale, encoding decisions, accessibility notes, and any unresolved limitations.

---

## Effective graph rules

1. Start with the reader question. "Visualize the data" is not a question.
2. Choose the chart by task, not by data shape alone.
3. Put the most important quantitative attribute on the most accurate available channel.
4. Use position on a common scale before length, length before angle, angle before area, area before luminance, and luminance before hue.
5. Use hue for category identity, not quantitative magnitude.
6. Use luminance or a sequential neutral ramp for ordered magnitude.
7. Use a diverging scale only when the data has a meaningful midpoint such as zero, target, baseline, or parity.
8. Use red for Northeastern brand emphasis and the primary series, not for "bad," "down," "danger," or "negative."
9. Use gold only for callout borders, figure accents, or decorative highlights. Never use gold as data fill.
10. Use direct labels when they reduce lookup work. Use legends only when direct labeling would clutter the chart.
11. Sort categories by the value that matters unless a natural, temporal, geographic, or official order is more meaningful.
12. Use small multiples when comparison across groups matters more than a single aggregate picture.
13. Show uncertainty when the claim depends on estimates, samples, forecasts, or model output.
14. Do not imply causality with correlation charts.
15. Do not smooth away structure unless the smoothing method is named and justified.
16. Do not decorate data marks. Decoration competes with evidence.
17. Remove every annotation that does not answer a question the reader has.
18. Prefer fewer stronger encodings over many weak encodings.
19. Never use 3D, perspective distortion, exploded pies, glossy effects, or decorative gradients in charts.
20. A chart that cannot be read at its deployment size has failed, even if it looks good full-screen.

---

## Marks and channels

### Mark types

| Mark | Use when | Common failure |
|---|---|---|
| Point | One observation or event | Overplotting hides density |
| Line | Ordered or continuous sequence | Implies continuity where none exists |
| Area | Accumulation, interval, polygon, or filled magnitude | Area magnitude is underestimated |
| Glyph | Multiple attributes in one symbol | Requires learning the symbol |
| Text | Labels, values, annotations | Too many labels become texture |
| Link | Relationship, flow, dependency | Hairball from too many edges |
| Polygon | Geographic or bounded regions | Region area competes with color encoding |

### Channel ranking for quantitative data

| Rank | Channel | Use for | Rule |
|---|---|---|---|
| 1 | Position on common scale | Primary quantitative comparison | Best default |
| 2 | Position on non-aligned scales | Small multiples, faceting | Keep scales documented |
| 3 | Length | Bars and intervals | Baseline matters |
| 4 | Angle or slope | Pie, radial, slope direction | Use sparingly |
| 5 | Area | Bubbles, treemaps, maps | Scale area honestly |
| 6 | Luminance | Secondary magnitude, choropleths | Limit steps and label |
| 7 | Hue | Category identity | Not for ranking |
| 8 | Shape or texture | Category identity or accessibility backup | Limit categories |

### Expressiveness principle

The channel must be capable of expressing the attribute type.

- Quantitative and ordered attributes belong on magnitude channels: position, length, area, luminance.
- Categorical attributes belong on identity channels: hue, shape, texture, line pattern.
- A quantitative attribute on hue is a channel mismatch.
- A categorical attribute on an ordered luminance ramp implies a false ranking unless the categories are genuinely ordered.

### Effectiveness principle

The most important attribute gets the highest-ranked channel appropriate to its type. If the reader's task is ranking values, do not hide the value in area, angle, hue, or tooltip-only interaction when position or length is available.

### Redundant encoding

Use redundant encoding when it helps accessibility, emphasis, or legend removal.

Good redundancy:
- Value encoded by bar length and direct label.
- Primary series encoded by red and line weight.
- Category encoded by x-position and direct text label.

Bad redundancy:
- Category encoded by x-position, hue, shape, and tooltip with no accessibility need.
- Quantitative value encoded by both bar length and unrelated hue.

---

## Northeastern visualization palette

Use the six-token palette from `DESIGN.md`. Do not invent new brand colors.

```css
--color-white:     #FFFFFF;
--color-ink:       #000000;
--color-red:       #C8102E;
--color-gold:      #A4804A;
--color-secondary: #555555;
--color-border:    #CCCCCC;
```

### Data roles

| Role | Token | Rule |
|---|---|---|
| Primary series | `--color-red` | Most important series only |
| Secondary series | `--color-ink` or `#404040` | Use for comparison or context |
| Neutral expansion | `#787878`, `#ADADAD` | Use grays before adding color |
| Sequential low | `#F5F5F5` | Near-white neutral |
| Sequential high | `--color-ink` | Black high end |
| Background | `--color-white` | White canvas |
| Gridline | `--color-border` at 60% opacity | Subordinate to data |
| Annotation accent | `--color-gold` | Border or underline only |

### Color rules

- Two data-encoding colors maximum before decomposing into small multiples, direct labels, patterns, or interaction.
- Red is brand, emphasis, and primary series. Red is not a semantic alert channel.
- Gold is never data fill and never body text.
- Quantitative scales use neutral luminance unless a specific semantic palette is approved.
- Categorical color is allowed only when category identity cannot be represented more clearly by position, grouping, label, or small multiple.
- No rainbow palettes.
- No bluish-purple palettes.
- No decorative gradients. Gradients are allowed only as explicit sequential or diverging scales.
- Every color-dependent chart must pass protanopia and deuteranopia review.

### Dark mode

Chart pantry files must support dark mode using the `DESIGN.md` tokens:

```css
@media (prefers-color-scheme: dark) {
  --color-white:     #111111;
  --color-ink:       #F0F0F0;
  --color-red:       #E8243A;
  --color-gold:      #C49A5A;
  --color-secondary: #999999;
  --color-border:    #333333;
}
```

Dark mode must preserve contrast, not invert meaning. Red remains the primary series. Gold remains decorative.

---

## Typography in charts

Follow `DESIGN.md`.

```css
font-family: 'Real Head Pro', 'FF Real', Lato, sans-serif;
```

JetBrains Mono is for code samples and technical file contents only. It is not used for axes, chart titles, legends, values, or annotations.

Never use Inter, Roboto, Arial, Helvetica, system-ui, Georgia, Times New Roman, EB Garamond, or other serif fonts in NEU chart output.

| Role | Size | Weight | Notes |
|---|---:|---:|---|
| Chart title | 16px | 700 | Top-left, sentence case |
| Chart subtitle | 13px | 400 | Secondary text |
| Axis tick | 11px | 400 | Minimum size |
| Axis title | 12px | 400 | Secondary text |
| Data label | 12px | 400 | Direct labels beat legends |
| Annotation | 12px | 400 | Short, precise |
| Tooltip | 13px | 400 | Not the only source of key data |
| Legend label | 12px | 400 | Avoid if direct labels work |
| Source line | 11px | 400 | All-caps permitted |

No ALL-CAPS headings beyond short eyebrow labels. No exclamation marks in authored chart copy.

---

## Axis, scale, and grid rules

### Axes

- Every quantitative axis must state unit, transformation, and domain when ambiguity is possible.
- Axis titles should be present unless the title, subtitle, and tick labels make the unit unmistakable.
- Tick labels must be formatted for the reader, not the data file: `12%`, `$1.2M`, `4.3x`, `2024`, not raw machine values.
- Do not rotate labels past -45 degrees. Use horizontal bars, wrapping, or small multiples instead.
- Gridlines are reference structure, not decoration. Use light neutral lines only.
- Remove gridlines when direct labels make them unnecessary.

### Scales

- Bars and area charts require a zero baseline.
- Line charts may use a nonzero y-axis when the chart is about change, not magnitude, but the axis must be labeled clearly.
- Log scales require explicit approval in the schema and must be named in the subtitle or axis.
- Diverging domains must be symmetric around the meaningful midpoint unless a documented reason says otherwise.
- Time scales must preserve actual time intervals. Do not evenly space irregular dates unless the chart is explicitly ordinal.
- Bubble radius must use `d3.scaleSqrt()` so area, not radius, is proportional to the data value.

### Proportional ink

The visual amount of ink must remain proportional to the data value whenever the mark is read as magnitude.

Required:
- Bar length starts at zero.
- Area chart fill starts at zero.
- Bubble area, not radius, maps to the value.
- Sankey, alluvial, and ribbon widths are proportional to flow values.
- Choropleths encode rates or ratios, not raw counts, unless the map is explicitly framed as count distribution and population bias is named.

---

## Chart selection grammar

Choose the chart family from the reader task.

| Reader task | Default family | First candidate |
|---|---|---|
| Compare categories | Comparison | Sorted bar chart |
| Show change over time | Time series | Line chart |
| Show distribution | Distribution | Histogram or box plot |
| Show relationship | Relationship | Scatterplot |
| Show components of a total | Part-to-whole | Stacked bar or waffle |
| Show nested structure | Hierarchy | Treemap or tree |
| Show movement between states | Flow | Sankey or alluvial |
| Show where | Spatial | Choropleth for rates, dot or bubble map for counts |
| Show financial OHLC | Specialized | Candlestick or OHLC |

The message can override the data structure. A budget table that sums to 100% is part-to-whole data, but if the reader question is "which category is largest?", the chart is a comparison chart.

---

## Chart family rules

### Comparison

- Use horizontal bars for long labels, usually more than 10-12 characters.
- Use vertical columns only when labels are short and categories are few.
- Sort by value for ranking tasks.
- Preserve official or temporal order when the order is meaningful.
- Bars start at zero. This is not negotiable.
- Grouped bars work for 2-4 subcategories per category.
- Stacked bars work when total and composition both matter.
- Use small multiples when cross-series comparison matters more than total.
- Dot plots work when a zero baseline would waste space and exact position matters.
- Radial bars are allowed only for cyclic data or explicitly rhetorical contexts. Linear bars win for precision.

### Change over time

- Use a line chart for trajectories through ordered time.
- Use area charts only when cumulative magnitude or filled volume matters. Area charts require zero baseline.
- Use stacked area when the total and composition over time both matter.
- Limit multi-line charts to about five prominent lines before using small multiples or interaction.
- Do not connect unordered categories with a line.
- Mark missing intervals as gaps. Do not interpolate silently.
- Smooth only when the smoothing method and window are documented.
- Use consistent time intervals. Irregular time spacing requires a real time scale.

### Distribution

- Use histograms for a single quantitative distribution, especially when `n > 50`.
- State binning method or bin count. Do not let bins decide the story silently.
- Use box plots for cross-group distribution comparison.
- Box plots use Tukey's 1.5 IQR whisker rule unless otherwise stated.
- Use violin or density plots when distribution shape and multimodality matter.
- Show raw points, jitter, or rug marks when sample size is small enough.
- Do not summarize a distribution with only mean bars when spread, skew, or outliers matter.

### Relationship

- Scatterplots require two quantitative attributes.
- Add trend lines only when the statistical model is appropriate and named.
- State correlation method when reporting correlation: Pearson, Spearman, Kendall, or other.
- Correlation is not causation. Do not imply intervention from association.
- Overplotting requires alpha, jitter, hexbin, contours, faceting, or sampling disclosure.
- Bubble charts use `d3.scaleSqrt()` for radius.
- Bubble charts need direct labels or tooltips for important points; area comparison is weak.
- Heatmaps use sorted categories where possible and a labeled color scale.

### Part-to-whole

- Pie charts are allowed for 2-5 slices with large differences and a simple share message.
- More than five slices usually becomes a sorted bar chart, stacked bar, or waffle chart.
- Donut charts need a center summary that earns the hole.
- Waffle charts are useful when percentage precision matters and categories are few.
- Stacked bars work best for 2-6 parts.
- Avoid asking readers to rank middle segments in stacked bars.
- Treemaps are part-to-whole plus hierarchy, not a replacement for precise ranking.
- Polar area charts must disclose the area/radius encoding and are rhetorical unless area-corrected.

### Hierarchy

- Treemaps work for regular depth, usually three levels or fewer in static output.
- Use `d3.treemapSquarify` unless another tiling method is explicitly justified.
- Sunbursts work when depth and path are the story. Too many levels become unreadable.
- Circle packing works for irregular depth but is weak for precise comparison.
- Tree diagrams work when exact topology matters more than quantitative area.
- Labels must not be clipped beyond recognition. Use tooltips or focus states for dense nodes.

### Flow and network

- Sankey diagrams show proportional flow. Link width must be proportional to value.
- Alluvial diagrams show flow across time or ordered stages.
- Chord diagrams show inter-entity flow. Use only when symmetry and reciprocity matter.
- Arc diagrams emphasize connections along a meaningful order.
- Force-directed layouts show structure, not exact distance. Do not over-interpret node position.
- Network charts need a hairball test: if clusters, bridges, or hubs are not readable, aggregate or filter.
- Node size, link width, color, and position must each encode a documented attribute or remain neutral.
- Do not encode importance with centrality unless the centrality metric is named.

### Spatial

- Choropleths encode rates, ratios, or normalized values. Raw counts usually belong in dot maps or bubble maps.
- Use an equal-area projection for choropleths: `d3.geoEqualEarth` for world maps, `d3.geoAlbersUsa` for US maps.
- Geographic area competes with color perception. Large regions will look more important.
- Class breaks must be named: quantile, quantize, natural breaks, threshold, or continuous.
- Use dot density for spatial distribution of counts.
- Use bubble maps for magnitude at locations. Radius must use `d3.scaleSqrt()`.
- Flow maps need origin, destination, direction, and magnitude documented.
- Maps are not default charts. If location is not part of the question, do not use a map.

### Specialized

- Candlestick and OHLC charts are for audiences who understand financial notation.
- Bullet graphs replace gauges for performance against target.
- Radar charts are allowed only for 3-7 dimensions and must document axis order.
- Parallel coordinates require interaction or strong ordering when dimensions exceed five.
- Calendar heatmaps work for daily temporal rhythms, not precise magnitude comparison.
- Gantt charts show planned or actual durations; dependencies need separate encoding.

---

## D3 implementation requirements for charts

Use `CLAUDE.md` for code structure. These visualization-specific rules also apply.

- Default D3 version is 7.9.0.
- Default deliverable is a standalone `.html` file with inline CSS, inline JS, and the pinned CDN.
- Use `ResizeObserver` and redraw from computed container dimensions.
- Use SVG for charts unless canvas is required for point volume or animation performance.
- Use `role="img"`, `aria-labelledby`, `<title>`, and `<desc>` on every SVG.
- Interactive marks must be keyboard-focusable when they reveal information not otherwise visible.
- Tooltips are enhancements, not the only place where core values live.
- Respect `prefers-reduced-motion: reduce`.
- Include empty and error states for loaded data.
- Use inline fallback data when loading a local JSON or CSV file for standalone portability.
- Do not silently filter rows. Any filtering must be documented in code and visible in notes.
- Use stable keys in `.data(data, d => d.id)` when updates, transitions, or interactions depend on object constancy.
- Do not use `d3.event`; D3 v7 event handlers receive `(event, d)`.
- Do not use pre-v4 API such as `d3.scale.linear()`.

---

## Prompt requirements for chart generation

Every chart prompt should include four moves.

### Move 1 - Show what you have

Name the data file, columns, sample rows, units, missing values, and transformations.

### Move 2 - Say what you want

Name the chart type, D3 version, output format, data-loading method, and deployment context.

### Move 3 - Constrain it

Specify:
- marks
- channel-to-attribute mappings
- sort order
- scale types
- axis domains
- baseline rules
- color roles
- labels, annotations, and legend behavior
- interaction behavior
- accessibility behavior

### Move 4 - Ask for verification

Ask Claude Code to restate the channel decomposition, name unspecified decisions, and generate code only after the specification is clear.

---

## Required chart audit before acceptance

Use this checklist for every chart, figure, dashboard tile, or interactive D3 file.

### Data and message

1. Reader question is stated in one sentence.
2. Unit of observation is clear.
3. Fields and types are documented.
4. Counts, rates, percentages, and indices are not mixed without labeling.
5. Denominators are stated for rates and percentages.
6. Missing data, filters, and transformations are documented.
7. The chart answers the stated question, not a different one.

### Encoding

8. Chart type matches the reader task.
9. Most important quantitative attribute uses the highest-ranked available channel.
10. No quantitative attribute is encoded by hue alone.
11. No categorical attribute is encoded by a magnitude channel unless the ordering is real.
12. Bars and area charts have zero baselines.
13. Bubble and symbol radius uses `d3.scaleSqrt()`.
14. Choropleths use rates or ratios unless count bias is explicitly named.
15. Diverging color has a meaningful midpoint.
16. Red is not used as "negative" or "danger."
17. Gold is not used as data fill.
18. Legends are replaced by direct labels when possible.

### Form and brand

19. Canvas, palette, and dark-mode tokens follow `DESIGN.md`.
20. Real Head Pro, FF Real, or Lato is used for all chart text.
21. JetBrains Mono is used only for code or technical file contents.
22. No unapproved colors, decorative gradients, 3D effects, or perspective distortions.
23. Gridlines are subtle and useful.
24. Tick labels are readable at deployment size.
25. Labels do not overlap or clip on desktop or mobile.
26. Annotation passes the removal test.

### Accessibility and runtime

27. SVG has `role="img"`, `<title>`, and `<desc>`.
28. Interactive marks expose equivalent information through focus or text.
29. Keyboard navigation reaches interactive elements in a logical order.
30. Color-blind review passes for protanopia and deuteranopia.
31. Contrast meets WCAG AA for text and essential marks.
32. `prefers-reduced-motion` suppresses animation.
33. Resize behavior works without overlap or layout breakage.
34. Empty, loading, and error states are present where data is loaded.
35. Browser console has no D3 API errors.

### Handoff

36. Data source is listed.
37. Transformation notes are listed.
38. Encoding rationale is listed.
39. Known limitations are listed.
40. The human has accepted the chart after visual review.

---

## What this visualization system never does

- No chart generation before data audit.
- No chart type chosen by the model without human confirmation.
- No encoding decision without a channel-to-attribute mapping.
- No red for alerts, losses, bad outcomes, or danger unless the human explicitly overrides the brand rule.
- No gold data series.
- No rainbow scales.
- No 3D chart effects.
- No pie chart with more than five slices.
- No bar chart without a zero baseline.
- No area chart without a zero baseline.
- No radius-linear bubbles.
- No raw-count choropleth without explicit warning.
- No dual y-axis unless explicitly approved and annotated.
- No smoothing without naming the method.
- No trend line without naming the model.
- No annotation that fails the removal test.
- No tooltip-only access to essential data.
- No unreadable mobile chart accepted as finished.

---

## Source of authority

This file is the data visualization constitution. It is loaded only when chart design, D3 visualization, statistical graphics, maps, dashboards, or visual analysis are in scope.

When in doubt, stop and write the audit. A chart built without an audit is a chart built on hope.
