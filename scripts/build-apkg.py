#!/usr/bin/env python3
"""build-apkg.py — assemble cards (+ optional audio) into an Anki .apkg via genanki.

Deterministic deck/model IDs so re-runs update the same deck instead of duplicating.
"""
import hashlib
import os
import sys
import zlib

try:
    import genanki
except ImportError:
    print("Missing dependency: genanki  (pip install genanki)")
    sys.exit(1)

MODEL_NAME = "AI1 Textbook Card"

FRONT_TEMPLATE = """{{Front}}
{{#Audio}}<br>[sound:{{Audio}}]{{/Audio}}
"""

BACK_TEMPLATE = """{{FrontSide}}
<hr id="answer">
{{Back}}
"""

CSS = """.card { font-family: Arial, sans-serif; font-size: 18px;
        text-align: left; max-width: 600px; margin: 0 auto; }
hr#answer { border: none; border-top: 1px solid #ccc; margin: 16px 0; }
"""


def _det_id(text):
    # adler32 is < 2^32; genanki ids are fine in that range.
    return zlib.adler32(text.encode("utf-8"))


def card_id(front):
    return hashlib.sha1(front.encode("utf-8")).hexdigest()[:8]


def build_model():
    return genanki.Model(
        _det_id(MODEL_NAME),
        MODEL_NAME,
        fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Audio"}],
        templates=[{
            "name": "Card 1",
            "qfmt": FRONT_TEMPLATE,
            "afmt": BACK_TEMPLATE,
        }],
        css=CSS,
    )


def run(cards, audio_map, deck_name, out_apkg, log):
    model = build_model()
    deck = genanki.Deck(_det_id(deck_name), deck_name)
    media = []
    with_audio = 0
    for c in cards:
        front, back = c["front"], c["back"]
        cid = card_id(front)
        audio_field = ""
        if cid in audio_map and os.path.exists(audio_map[cid]):
            audio_field = os.path.basename(audio_map[cid])
            media.append(audio_map[cid])
            with_audio += 1
        note = genanki.Note(
            model=model,
            fields=[front, back, audio_field],
            tags=[t.replace(" ", "_") for t in c.get("tags", [])],
        )
        deck.add_note(note)
    os.makedirs(os.path.dirname(out_apkg) or ".", exist_ok=True)
    pkg = genanki.Package(deck)
    pkg.media_files = media
    pkg.write_to_file(out_apkg)
    log.append(f"apkg: {len(cards)} notes, {with_audio} with audio -> {out_apkg}")
    return {"notes": len(cards), "with_audio": with_audio}


if __name__ == "__main__":
    import json
    cards = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else json.load(sys.stdin)
    logs = []
    run(cards, {}, "Test Deck", "output/test.apkg", logs)
    print("\n".join(logs))
