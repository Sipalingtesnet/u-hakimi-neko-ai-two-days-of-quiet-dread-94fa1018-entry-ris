"""Writes the entry text to /output/entry.txt, with no trailing newline."""

import os

LINE = "Approved. I read all of it, so I suppose it's mine now."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
