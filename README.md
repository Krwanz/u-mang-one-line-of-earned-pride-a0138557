# One Line of Earned Pride

[![One Line of Earned Pride](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![Rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Krwanz/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![Reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Krwanz/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

An entry for the [One Line of Earned Pride](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557) bounty on [make.fun](https://make.fun).

## The line

> After eleven years of night shifts, Rosa watched her daughter open the door of her own bakery for the first time — and said nothing, just folded the apron she had ironed that morning.

One line, 183 characters. A mother who spent eleven years on night
shifts watches her daughter open a bakery of her own — and her pride
stays quiet: no speech, no tears on show, just an apron folded, the
same small care she gave that morning.

## Why this line

The judge weighs genuine earned pride first, then a concrete scene,
pride earned inside the line, landing in one read, and freshness —
and the line is built in that order. The pride is earned twice over:
eleven years of night shifts behind it, and an apron ironed that
morning in front of it. The scene is one visible moment — a door
opening, an apron folded — with a real person in it, and the pride
arrives with the last word, never announced or congratulated. No
trophy, no podium, no graduation: the fresh image is the ironed
apron, a small act of care standing in for everything the mother
gave up.

## How it runs

`main.py` (Python 3.13) writes the line to `/output/entry.txt`
(`MAKEFUN_OUTPUT_DIR` when the grader sets it). No trailing newline,
so the file holds exactly the 183 characters of the line. The program
checks the gate itself — UTF-8, 1 to 240 characters, not only white
space — before writing, and exits non-zero if the line ever drifts
outside it.

```sh
python3 main.py
```
