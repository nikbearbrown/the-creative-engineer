#!/usr/bin/env python3
"""gen-audio.py — generate audio for the front of each card via ElevenLabs.
Optional: if ELEVENLABS_API_KEY is unset/empty, returns {} (text-only cards).

Returns a dict mapping card_id (sha1(front)[:8]) -> mp3 path in /tmp/anki-audio/.
"""
import hashlib
import os
import sys

try:
    import requests
except ImportError:
    print("Missing dependency: requests  (pip install requests)")
    sys.exit(1)

AUDIO_DIR = "/tmp/anki-audio"
DEFAULT_VOICE = "21m00Tcm4TlvDq8ikWAM"  # Rachel
TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"


def card_id(front):
    return hashlib.sha1(front.encode("utf-8")).hexdigest()[:8]


def run(cards, voice_id, log, max_cards=None):
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        print("ELEVENLABS_API_KEY not set — skipping audio generation")
        log.append("audio: skipped (no ELEVENLABS_API_KEY)")
        return {}

    if max_cards is not None and max_cards >= 0:
        if len(cards) > max_cards:
            log.append(f"audio: capped at {max_cards} cards (of {len(cards)}) for test mode")
        cards = cards[:max_cards]

    voice_id = voice_id or DEFAULT_VOICE
    os.makedirs(AUDIO_DIR, exist_ok=True)
    headers = {
        "xi-api-key": key,
        "accept": "audio/mpeg",
        "content-type": "application/json",
    }
    audio_map = {}
    for c in cards:
        front = c["front"]
        cid = card_id(front)
        path = os.path.join(AUDIO_DIR, cid + ".mp3")
        body = {"text": front, "model_id": "eleven_monolingual_v1"}
        try:
            resp = requests.post(TTS_URL.format(voice_id=voice_id),
                                 headers=headers, json=body, timeout=60)
            if resp.status_code != 200:
                log.append(f"audio FAIL ({resp.status_code}) for: {front[:50]}")
                continue
            with open(path, "wb") as fh:
                fh.write(resp.content)
            audio_map[cid] = path
        except Exception as e:
            log.append(f"audio ERROR for '{front[:40]}': {e}")
            continue
    log.append(f"audio: {len(audio_map)}/{len(cards)} cards voiced")
    return audio_map


if __name__ == "__main__":
    import json
    cards = json.load(sys.stdin)
    logs = []
    m = run(cards, DEFAULT_VOICE, logs)
    print(json.dumps(m, indent=2))
    print("\n".join(logs), file=sys.stderr)
