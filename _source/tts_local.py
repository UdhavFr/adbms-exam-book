"""Run the Papermorph tts.py pipeline without ffprobe (pure-Python MP3 duration).

Usage: python _source/tts_local.py content/adbms/ch19/narration.en.json site/adbms/ch19/audio/en
"""
import importlib.util
import sys
from pathlib import Path

SKILL_TTS = Path(__file__).resolve().parents[1] / "_papermorph" / ".claude" / "skills" / "papermorph" / "scripts" / "tts.py"

BR = {0: None, 1: 32, 2: 40, 3: 48, 4: 56, 5: 64, 6: 80, 7: 96, 8: 112,
      9: 128, 10: 160, 11: 192, 12: 224, 13: 256, 14: 320, 15: None}
SR = {(3, 0): 44100, (3, 1): 48000, (3, 2): 32000,
      (2, 0): 22050, (2, 1): 24000, (2, 2): 16000,
      (0, 0): 11025, (0, 1): 12000, (0, 2): 8000}


def mp3_duration(path):
    data = Path(path).read_bytes()
    n = len(data)
    pos = 0
    if data[:3] == b"ID3":
        size = 0
        for b in data[6:10]:
            size = (size << 7) | (b & 0x7F)
        pos = 10 + size
    total = 0.0
    frames = 0
    while pos + 4 <= n:
        if data[pos] == 0xFF and (data[pos + 1] & 0xE0) == 0xE0:
            ver = (data[pos + 1] >> 3) & 0x03
            layer = (data[pos + 1] >> 1) & 0x03
            bi = (data[pos + 2] >> 4) & 0x0F
            si = (data[pos + 2] >> 2) & 0x03
            pad = (data[pos + 2] >> 1) & 0x01
            br = BR.get(bi)
            sr = SR.get((ver, si))
            if layer == 1 and br and sr and ver != 1:
                if ver == 3:
                    flen, samples = int(144 * br * 1000 / sr + pad), 1152
                else:
                    flen, samples = int(72 * br * 1000 / sr + pad), 576
                if flen > 0 and pos + flen <= n + 1:
                    total += samples / sr
                    frames += 1
                    pos += flen
                    continue
        pos += 1
    if not frames:
        raise ValueError(f"no MPEG Layer-III frames found in {path}")
    return round(total, 3)


spec = importlib.util.spec_from_file_location("pm_tts", SKILL_TTS)
tts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tts)
tts.duration = mp3_duration

if __name__ == "__main__":
    import asyncio
    asyncio.run(tts.main(*sys.argv[1:3]))
    # sanity: duration must exceed the last spoken word of every beat
    import json
    out = Path(sys.argv[2])
    timings = json.loads((out / "timings.js").read_text(encoding="utf-8").split("=", 1)[1])
    cache = json.loads(Path(sys.argv[1]).with_suffix(".timings.json").read_text(encoding="utf-8"))
    for beat, entry in timings.items():
        words = cache[beat]["words"]
        last = max((w[0] for w in words), default=0)
        status = "OK " if entry["dur"] >= last else "BAD"
        print(f"{status} {beat}: dur={entry['dur']}s last-word={round(last,2)}s marks={entry['marks']}")
