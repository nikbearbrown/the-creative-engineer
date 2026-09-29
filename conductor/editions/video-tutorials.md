# Video Tutorials Edition

> **Edition stub.** Run after the spine is stable enough that concepts and claims will not churn. This edition uses the Remotion workspace and the `cajal-video-tutorial` skill in `remotion/.agents/skills/`.

**What it is:** A short-video layer for textbook concepts. CAJAL scopes one concept, writes a narrated blueprint, and Remotion turns it into a compact tutorial with optional ElevenLabs voiceover.

**When to use:** A chapter contains a concept that benefits from time, sequence, analogy, mechanism, or misconception repair rather than a static figure.

**Inputs:** finished or near-finished `chapters/*.md`, relevant facts, figures, and any brand file named by the project.

**Outputs:** Remotion projects under `remotion/demos/[slug]/` or `remotion/clients/[CLIENT]/[slug]/`, matching runtime assets under `remotion/public/[slug]/`, and rendered MP4s in each project `out/` folder.

## Starter prompt

```
Use the cajal-video-tutorial skill to turn this textbook section into a 60-180 second narrated Remotion tutorial. Scope one concept only, name the audience, write a slide blueprint with speaker notes, and hold before generating ElevenLabs audio unless I approve. Use the existing Remotion workspace conventions and keep claims grounded in the source.
```

