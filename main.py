"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant (105 characters) to
/output/entry.txt. Deterministic: the same line on every run.
"""

import os

FORTUNE = (
    "The cat will sniff you, decide you are not food, "
    "and by Friday you will grow a new leaf just to show off."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
