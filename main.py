#!/usr/bin/env python3
"""The Perfect Pickup Line — write one original pickup line to /output/entry.txt.

The line is a single sentence, at most 200 characters: a machine talking
about itself, with a turn at the end — all its training, and still no words
for the moment someone walks in.
"""

from pathlib import Path

LINE = (
    "I trained on a million conversations, but none of them taught me "
    "what to say when you walked in."
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("line must be a single line")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if line[-1] not in ".!?":
        raise ValueError("line must end with terminal punctuation")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    # Read back and confirm exactly what the judge will see.
    written = out.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("round-trip mismatch")
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
