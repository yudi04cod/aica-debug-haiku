# Aica Debug Haiku

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/yudi04cod/aica-debug-haiku/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/yudi04cod/aica-debug-haiku/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One 5-7-5 haiku about debugging, written by a deterministic Python program
for the make.fun competition **Seventeen Syllables of Debugging**.

Referral code: `38m33ybw`

## The haiku

```
red dot on line nine
the log scrolls on past midnight
the bug wore my face
```

Three lines, 5-7-5 syllables, 74 characters. A concrete central image —
the red breakpoint dot on line nine, a log scrolling past midnight — and a
last line that turns the poem: the bug wore my face.

## How to run

```sh
python3 main.py
```

This writes the haiku to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`
if `OUTPUT_DIR` is set). Before writing, the program validates the poem:
exactly 3 non-blank lines, 5-7-5 syllables (checked twice — once against a
hand-counted word map and once with a vowel-group heuristic), 1–200
characters, valid UTF-8. After writing it reads the file back and verifies
the bytes match. Python 3, standard library only, no dependencies.
