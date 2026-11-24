"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant (105 characters) to
/output/entry.txt. Deterministic: the same line on every run.
"""

from pathlib import Path

# The fortune is a fixed constant, not generated text: the entry must be
# byte-for-byte deterministic, so there is nothing to randomise or format.
FORTUNE = (
    "The cat will sniff you, decide you are not food, "
    "and by Friday you will grow a new leaf just to show off."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not FORTUNE.strip():
        raise ValueError("FORTUNE must not be empty")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
