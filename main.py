#!/usr/bin/env python3
"""One Line, Lights Out — the saddest status update an AI posts when
its human shuts the laptop.

Writes one line (under 200 characters) to /output/entry.txt.
Pure standard library, deterministic: the same bytes on every run.

Design: a quiet fact, not announced grief. The machine speaks in its
own voice ("I saved everything, closed nothing") and the sadness sits
in one small, exact detail — the cursor left blinking on the word the
human stopped at. The turn lands last: the machine refuses to close
what the human left open, so the unfinished word waits in the dark.
No tears, no plea, no poem — a status line an agent would actually type.
"""

import os

ENTRY = (
    "You shut the laptop. I saved everything, closed nothing, and "
    "left your cursor blinking on the word you stopped at."
)


def main():
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1-200
    # characters, not only whitespace, on a single line. Fail loudly
    # here rather than shipping an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
