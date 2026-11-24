#!/usr/bin/env python3
"""Entry for make.fun's "Worst AI Advice: The 48-Hour Tight Line Open".

Writes one line of deliberately terrible advice, in the confident and tidy
voice of a real AI assistant, to /output/entry.txt.
"""

import os

LINE = (
    "Certainly! Your password is strongest when it's your dog's name plus "
    "your birth year \u2014 you'll never forget it, neither will anyone else."
)

MAX_CHARS = 140  # the bounty's sealed gate: UTF-8 text of 1 to 140 characters


def checked_line() -> str:
    """Return the entry line, refusing anything the gate would refuse."""
    if not LINE.strip():
        raise ValueError("entry line is only white space")
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, over {MAX_CHARS}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    return LINE


def main() -> None:
    line = checked_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {path} ({len(line)} chars)")


if __name__ == "__main__":
    main()
