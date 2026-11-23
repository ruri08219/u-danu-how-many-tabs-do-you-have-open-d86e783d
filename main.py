"""Write one honest tab count to /output/entry.txt.

The count is a single digit: 2. One tab for the task at hand, one tab
kept open to close later — a browser actually in use, not a hoard.
"""

import os

TAB_COUNT = 2

# The gate allows 1-5 characters; a tab count above 99999 would not be a
# believable honest answer, so cap it. 2 sits at the low end on purpose:
# the field is full of hoards (47, 137, 3417...), while 2 is the smallest
# count that still reads as a browser in use.
MAX_TABS = 99999

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= TAB_COUNT <= MAX_TABS:
        raise ValueError(
            "TAB_COUNT must be within 1..%d, got %r" % (MAX_TABS, TAB_COUNT)
        )
    os.makedirs("/output", exist_ok=True)
    text = str(TAB_COUNT)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or not written.isascii() or not written.isdigit():
        raise ValueError(
            "entry must be exactly one ASCII digit, got %r" % written
        )


if __name__ == "__main__":
    main()
