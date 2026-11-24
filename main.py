#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

Writes exactly one word to /output/entry.txt: apophenia.

Why this word: apophenia is the tendency to see meaningful patterns in
random noise, faces in clouds, messages in static. It is surprising
because it is a psychology term, not a word from the usual beautiful-word
lists. It is vivid because almost everyone has caught themselves doing
it. And it carries a small joke: a technical word for inventing meaning
where there may be none, doing exactly what it names.
"""

import os
import sys

WORD = "apophenia"


def validate(word):
    """Enforce the bounty gate before anything is written.

    The gate accepts UTF-8 text of 1 to 24 characters, not only white
    space, and the judge only ever sees exactly one word, so the entry
    must also hold a single token with no whitespace inside it.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1 to 24 characters, got %d" % len(word))
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")
    return True


def main():
    validate(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise ValueError("written entry does not match the chosen word")
    return 0


if __name__ == "__main__":
    sys.exit(main())
