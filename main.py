"""The One-Line Laugh — entry v2 (final).

Writes a single funny line (one sentence, <= 200 chars) to /output/entry.txt.
Deterministic, stdlib only, no network.

The line: a password reset everyone has lived through. The setup is the
universal ritual (forced expiry, the lazy tweak); the punchline lands at
the very end — "we both pretend" — turning the system into a co-conspirator
in the same small lie. Surprise at the end, an everyday truth, every word
earning its place, and a framing (mutual pretence) that is not the usual
password joke.
"""

import os

LINE = (
    "My password expired, so I changed it to the same one with a capital "
    "letter, and now we both pretend it's secure."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-200 characters"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
