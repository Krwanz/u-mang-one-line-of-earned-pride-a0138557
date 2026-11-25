"""One Line of Earned Pride — entry program (Python 3.13).

Writes a single line of text to /output/entry.txt (the directory the
grader names in MAKEFUN_OUTPUT_DIR). The line must be UTF-8 text of
1 to 240 characters, not only white space. The program checks that
itself before writing and fails loudly if the line ever drifts out
of the gate, so a bad line can never be submitted silently.
"""

import os
import sys

LINE = (
    "After eleven years of night shifts, Rosa watched her daughter "
    "open the door of her own bakery for the first time \u2014 and said "
    "nothing, just folded the apron she had ironed that morning."
)


def main() -> int:
    if not (1 <= len(LINE) <= 240):
        print(f"entry is {len(LINE)} characters, outside the 1-240 gate",
              file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
