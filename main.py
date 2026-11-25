"""One-Line Office Joke Laugh-Off entry (Python 3.13, standard library only).

Writes a single one-line office joke to /output/entry.txt. Outside the
grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The entry line is held in the LINE constant below and written verbatim,
with no trailing newline, so the file is exactly the joke: 98 UTF-8
characters, inside the competition gate of 1 to 200 characters, and not
only white space. The program is deterministic: it writes the same bytes
on every run, and it self-checks the written file against LINE before it
exits, raising if the two ever disagree.
"""

import os

LINE = "The office plant died, so now it's the only thing here that isn't expected to grow under pressure."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    """Write the entry line, exactly, to entry.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # Self-check: the file must hold the line, byte for byte.
    with open(target, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        raise RuntimeError("entry.txt does not match LINE")


if __name__ == "__main__":
    main()
