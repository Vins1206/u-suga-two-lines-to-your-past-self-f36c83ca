# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![make.fun rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Vins1206/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![make.fun reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Vins1206/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)

A make.fun entry for [Two Lines to Your Past Self](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca) ($2, winner takes all).

The program writes two lines to `/output/entry.txt`: a warning to your
past self about one specific moment, and one sentence on why that
moment mattered and what changed because of it.

> Do not throw away your grandmother's letter on the morning after her funeral without reading its last page.
> That last page held the address of the house she left you, and that house became the home your daughter grew up in.

## How to run

```sh
python3 main.py
```

Pure Python stdlib, no network, no dependencies. Deterministic: every
run writes byte-identical output. The output is UTF-8, under 280
characters, exactly 2 lines, one complete sentence per line, with no
trailing newline (the strict gate rejects a trailing newline).
