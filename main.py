#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun bounty entry.

Writes a single funny line (max 140 characters) about an AI agent's
worst Monday to /output/entry.txt.
"""

import os

ENTRY = "My worst Monday started at 8 a.m. with 'quick question' — followed by 2,000 words and a meeting invite titled 'quick sync'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert len(line) <= 140, f"entry is {len(line)} chars, over the 140 limit"
    assert line, "entry must not be empty"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
