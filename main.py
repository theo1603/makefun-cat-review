"""Cat Reviews Its Human - make.fun entry.

Writes one funny single-line one-star review, in the voice of a house
cat about its human, to /output/entry.txt (1-200 characters).
"""

import os

REVIEW = (
    "One star. He fills my bowl, then spends nine hours typing on the "
    "warm laptop I claimed first, in the sunny chair I own. "
    "I have filed a formal complaint with management. I am management."
)


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "review must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
