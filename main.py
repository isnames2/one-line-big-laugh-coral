"""One Line, Big Laugh — a single hilarious line, 200 characters or fewer.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python standard library; output is byte-identical on every run.
"""

import os
from pathlib import Path

LINE = (
    "My smartwatch says my heart rate spikes every time I check "
    "my bank balance. It's the only cardio I get."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters (RULES.txt).
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
