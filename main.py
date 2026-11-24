#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the entrant. Standard library only, no randomness, no clock,
no network — fully deterministic.
"""

import os

WORD = "placeholder"  # revised 2026-11-24 ~20:58 WIB, new session:
# sharper than "forgettable" — a placeholder was never the real thing,
# just a stand-in until someone better came along. Funnier, more vivid,
# and less generic, while still painfully honest and instantly landing.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
