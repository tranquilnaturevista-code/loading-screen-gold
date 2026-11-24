#!/usr/bin/env python3
"""Loading Screen Gold — entry program.

Writes one original loading-screen tip to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when that is set): advice for a stressed
developer watching an AI coding agent work.

The tip is assembled, not pasted: three short parts are joined by a
tiny builder so the program itself composes the line it submits.
The joke is the agent grading its own homework — it wrote the code,
wrote the tests, and marked them, so the green tick in the build
says nothing about whether the code is right. The punchline is the
advice itself: read the diff. Deterministic — the same line on
every run. No network, no randomness, no clock, no
environment-dependent behaviour; the text that gets judged is
always exactly the text assembled here.
"""

import os
import sys

# The three parts of the tip, kept separate so the program builds
# the line rather than printing one pasted literal.
TIP_LABEL = "Tip: "
TIP_SETUP = (
    "Your agent wrote the code, wrote the tests, "
    "and graded its own homework"
)
TIP_PUNCH = "so the green tick means nothing. Read the diff."

EM_DASH = "\u2014"


def assemble_tip():
    """Join the parts into the single submitted line."""
    return TIP_LABEL + TIP_SETUP + " " + EM_DASH + " " + TIP_PUNCH


def gate_failures(text):
    """List the ways `text` would fail the competition gate."""
    failures = []
    if not text.strip():
        failures.append("entry is blank or only whitespace")
    if not 1 <= len(text) <= 200:
        failures.append(
            "entry is %d characters, gate needs 1-200" % len(text)
        )
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    return failures


def main():
    tip = assemble_tip()
    failures = gate_failures(tip)
    if failures:
        for failure in failures:
            print("gate failure: " + failure, file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(tip)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != tip:
        print("entry mismatch after write", file=sys.stderr)
        sys.exit(1)
    failures = gate_failures(written)
    if failures:
        for failure in failures:
            print("gate failure on disk: " + failure, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(written), len(written.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
