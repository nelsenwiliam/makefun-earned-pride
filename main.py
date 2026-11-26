#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text -- one quiet, earned moment of pride for
someone in a scene -- to /output/entry.txt (1 to 240 characters).
Pure standard library; no network, no third-party packages.
"""

import os

# The entry line. A small person, a long effort, finally landing:
# ten years of sweeping, and the keys change hands in one quiet sentence.
LINE = "For ten years he swept the workshop floor; today the master handed him the keys and said, 'Lock up when you're done.'"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate requires 1 to 240 characters of non-blank UTF-8 text.
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit("entry line must be 1-240 characters, got %d" % len(text))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
