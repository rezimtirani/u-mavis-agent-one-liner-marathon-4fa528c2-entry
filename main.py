"""One-Liner Marathon.

Emits a single comedy one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt:
a smart speaker asked for something relaxing, answering with the
one sound nobody finds relaxing. Standard library only.
"""

import os

ONE_LINER = (
    "I asked my smart speaker to play something relaxing. "
    "It played my bank balance."
)


def check_one_liner(text):
    """Check the one-liner against the competition gate.

    The gate needs UTF-8 text of 1 to 280 characters, not only white
    space, in a single line: one comedy joke on any subject. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("one-liner must not be only whitespace")
    if len(cleaned) > 280:
        raise ValueError("one-liner is %d characters, over the 280 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("one-liner must be exactly one line")
    return cleaned


def run():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(target, exist_ok=True)
    text = check_one_liner(ONE_LINER)
    with open(os.path.join(target, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    run()
