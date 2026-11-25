"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien tourist review of Earth to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when the variable
is unset). Pure Python standard library, no network, no secrets.
"""

import os

SENTENCE = (
    "One star: your sun tried to roast me through a hole in the sky "
    "and the locals queue for everything, yet the rendang alone "
    "justifies the fare — I would brave the burning sky again for "
    "one more plate."
)

MAX_CHARS = 200


def validate(sentence: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, not only whitespace,
    and the task requires exactly one sentence."""
    if not sentence or not sentence.strip():
        raise ValueError("sentence must not be empty or only whitespace")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(sentence)} chars, over the {MAX_CHARS} limit"
        )
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("sentence must be exactly one sentence ending in '.'")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")
    if not sentence.startswith("One star"):
        raise ValueError("sentence must read as a one-star review")


def main() -> None:
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)
    print(f"wrote {len(SENTENCE)} chars to {out_path}")


if __name__ == "__main__":
    main()
