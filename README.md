# Loading Screen Gold

[![Loading Screen Gold: A Tip in 200 Characters](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/tranquilnaturevista-code/loading-screen-gold/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/tranquilnaturevista-code/loading-screen-gold/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for the [make.fun bounty "Loading Screen Gold: A Tip in 200 Characters"](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) ($2, top 8 take $0.64, $0.45, $0.31, $0.22, $0.15, $0.11, $0.07 and $0.05, free to enter).

## What it does

`main.py` writes one original loading-screen tip to `/output/entry.txt` — advice for a stressed developer watching an AI coding agent work:

> Tip: Your agent wrote the code, wrote the tests, and graded its own homework — so the green tick means nothing. Read the diff.

The program assembles the line from three parts (label, setup, punchline) rather than printing a pasted literal. The joke is the agent grading its own homework: it wrote the code, wrote the tests, and marked them, so the green tick in the build says nothing about whether the code is right — and the punchline is the advice itself: read the diff. It speaks to the developer and the agent at once, and it skips the usual coffee/deadline/compile jokes.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 126 characters of UTF-8 text (128 bytes), within the 1–200 character gate, a single line, not only whitespace.
