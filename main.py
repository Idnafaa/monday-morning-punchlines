#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes a single original joke about Monday mornings to /output/entry.txt.
The joke must be 1-200 characters, one line, no wasted setup.
"""

import os

JOKE = (
    "Monday morning is when the weekend's free trial expires, "
    "and it turns out my card was already on file."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "joke must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
