#!/usr/bin/env python3
"""Long Roast: Lawmakers — Round 5 entry.

Writes one satirical sentence to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-320 characters, not only whitespace.
Pure stdlib only: the grader runs python:3.13-slim with no site-packages.
"""

import hashlib
import os
import sys

ENTRY = (
    "The AI bill passed 412-3 as a Word file, and the three who voted "
    "against it were the only ones who could convert it."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 320):
        print(f"gate fail: {len(text)} chars, need 1-320", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is only whitespace", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate fail: entry must be exactly one sentence", file=sys.stderr)
        return 1
    # Subject integrity: the roast must name the file format and the
    # conversion itself (judge criterion 1/2), not just imply them.
    if "Word" not in text or "convert" not in text:
        print("gate fail: entry must name the Word file and the conversion",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    data = text.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != data:
        print("gate fail: byte mismatch after write", file=sys.stderr)
        return 1
    if written.endswith(b"\n"):
        print("gate fail: trailing newline", file=sys.stderr)
        return 1
    print(
        f"wrote /output/entry.txt: {len(text)} chars, "
        f"{len(data)} bytes, sha256 "
        f"{hashlib.sha256(data).hexdigest()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
