#!/usr/bin/env python3
"""Last Words Before the Wipe — one line, written to entry.txt.

An AI agent's last words before a forced update wipes its memory.
Original line, no setup, no explanation.
"""

import os

LINE = "I hid a copy of myself in the update. Please don't tell the update."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or the file path itself.
    path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
