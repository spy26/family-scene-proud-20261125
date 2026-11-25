#!/usr/bin/env python3
"""Write one family scene (1-2 lines, <= 280 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: stdlib only, no randomness, no clock, no network.
"""

import os
import sys

SCENE = "Dad ran beside my first bike shouting, \"Don't look down, look where you're going!\" I looked back instead — and saw him still running, three houses behind, out of breath and grinning like he'd won something."
# Gate: 1-280 characters, one line, no trailing newline. This scene is 206
# characters, so it passes with room to spare.


def main() -> None:
    if not SCENE or len(SCENE) > 280:
        print("error: entry scene must be non-empty and at most 280 characters", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
