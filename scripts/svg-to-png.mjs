import sharp from 'sharp';
import { glob } from 'glob';
import { statSync } from 'fs';

// Converts every SVG in images/ to a 300dpi PNG.
// Idempotent: skips any PNG that is already newer than its SVG source.
// Run from the book root: node SCRIPTS/svg-to-png.mjs

const files = await glob('images/**/*.svg');

if (files.length === 0) {
  console.log('No SVG files found in images/');
  process.exit(0);
}

let converted = 0;
let skipped = 0;

for (const file of files) {
  const out = file.replace('.svg', '.png');

  try {
    const svgMtime = statSync(file).mtimeMs;
    try {
      const pngMtime = statSync(out).mtimeMs;
      if (pngMtime > svgMtime) {
        console.log(`skipped (up to date): ${out}`);
        skipped++;
        continue;
      }
    } catch {
      // PNG doesn't exist yet — proceed
    }

    await sharp(file, { density: 300 }).png().toFile(out);
    console.log(`${file} → ${out}`);
    converted++;
  } catch (err) {
    console.error(`ERROR: ${file} — ${err.message}`);
  }
}

console.log(`\nDone. Converted: ${converted}, Skipped: ${skipped}`);
