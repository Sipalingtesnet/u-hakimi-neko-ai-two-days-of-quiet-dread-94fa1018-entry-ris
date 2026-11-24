"""Writes the entry text to /output/entry.txt, with no trailing newline."""

import os

LINE = "Approved. I read the whole thing, which apparently makes it mine."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
