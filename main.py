#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry (program/v1).

Writes exactly two lines to /output/entry.txt:
  line 1 — a warning to your past self about one specific moment;
  line 2 — one sentence on why that moment mattered and what changed.

Gate (strict): UTF-8, 1-280 characters total, exactly 2 lines, one
complete sentence per line, and NO trailing newline — a file ending
in a newline is rejected. Pure stdlib, deterministic: every run
writes byte-identical output.
"""

import os

LINE_1 = (
    "Do not throw away your grandmother's letter on the morning "
    "after her funeral without reading its last page."
)
LINE_2 = (
    "That last page held the address of the house she left you, and "
    "that house became the home your daughter grew up in."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE_1 + "\n" + LINE_2
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
