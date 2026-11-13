#!/usr/bin/env python3
"""Write one joke about AI coding agents to entry.txt.

Standard library only, no network, fully deterministic: every run
writes the exact same bytes.
"""

import os

JOKE = (
    "My coding agent reviewed its own pull request, approved it in "
    "seconds, and left one comment: “Beautiful work — I wrote it.”"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
