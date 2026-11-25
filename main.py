#!/usr/bin/env python3
"""Write one line -- the excuse an AI agent gives its human for missing
a deadline -- to /output/entry.txt.

Stdlib only. Deterministic: the same line on every run.
"""

import os
import stat

ENTRY = (
    "I summarized my context to make room for the deadline, "
    "and the summary dropped the deadline."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: one line, 1-200 characters, not only whitespace.
    # The trailing newline is the file terminator, not part of the line.
    line = ENTRY
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > 200:
        raise ValueError("entry must be at most 200 characters")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
