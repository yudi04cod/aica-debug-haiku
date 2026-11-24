#!/usr/bin/env python3
"""Write one 5-7-5 haiku about debugging to /output/entry.txt.

Deterministic, stdlib only. Validates the poem before writing, then
reads the file back and verifies the bytes match what was written.
"""

import os
import sys

# The haiku. Syllable counts verified by hand:
#   red(1) dot(1) on(1) line(1) nine(1)                    -> 5
#   the(1) log(1) scrolls(1) on(1) past(1) mid-night(2)    -> 7
#   the(1) bug(1) wore(1) my(1) face(1)                    -> 5
# (The draft line "the log scrolls past midnight" was only 6
# syllables; adding "on" brings line 2 to 7.)
HAIKU = [
    "red dot on line nine",
    "the log scrolls on past midnight",
    "the bug wore my face",
]

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_CHARS = 200


def count_syllables(word):
    """Count syllables for a single simple English word.

    Hand-tuned for the vocabulary of this haiku: count vowel groups,
    treat a silent trailing 'e' as silent, and handle the word
    'midnight' (two vowel groups) naturally. This is a heuristic, not
    a dictionary lookup — so the words used here are pinned by an
    explicit expected map in WORD_SYLLABLES and checked separately.
    """
    word = word.lower().strip(".,;:!?\"'")
    vowels = "aeiouy"
    count = 0
    prev_is_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_is_vowel:
            count += 1
        prev_is_vowel = is_vowel
    # Silent trailing 'e' (e.g. "line", "face") is not a syllable.
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


# Ground truth for every word in the haiku, counted by hand.
WORD_SYLLABLES = {
    "red": 1, "dot": 1, "on": 1, "line": 1, "nine": 1,
    "the": 1, "log": 1, "scrolls": 1, "past": 1, "midnight": 2,
    "bug": 1, "wore": 1, "my": 1, "face": 1,
}


def validate(text):
    """Raise AssertionError if the haiku violates any competition rule."""
    body = text.rstrip("\n")
    lines = body.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "blank line in haiku"
    assert 1 <= len(body) <= MAX_CHARS, (
        f"haiku must be 1-{MAX_CHARS} chars, got {len(body)}"
    )
    for i, (line, want) in enumerate(zip(lines, EXPECTED_SYLLABLES)):
        words = line.split()
        got_map = sum(WORD_SYLLABLES[w.lower()] for w in words)
        got_heur = sum(count_syllables(w) for w in words)
        assert got_map == want, (
            f"line {i + 1}: expected {want} syllables, got {got_map}"
        )
        # The heuristic and the hand-counted map must agree.
        assert got_heur == got_map, (
            f"line {i + 1}: heuristic {got_heur} != hand count {got_map}"
        )
    return body



def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    # --- validation, before anything is written ---
    body = validate("\n".join(HAIKU))
    text = body + "\n"

    # --- write, then read back and verify byte-for-byte ---
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    with open(out_path, "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "read-back mismatch"
    assert written.decode("utf-8") == text, "read-back is not valid UTF-8 text"

    print(f"wrote {out_path} ({len(body)} chars, 3 lines, 5-7-5)")
    print(text, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
