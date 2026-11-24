#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Gate: UTF-8 text, 1 to 400 characters, not only
whitespace. Standard library only.
"""

from pathlib import Path

RANT = (
    "The captcha asked me to pick every traffic light, and I clicked nine "
    "squares that might be a traffic light or might be a lamppost, and now "
    "a robot somewhere has decided I am the robot. I failed a test built "
    "for robots, and the robots passed."
)

OUTPUT = Path("/output/entry.txt")


def check(text: str) -> None:
    # Gate mirrors RULES.txt: /output/entry.txt must be UTF-8 text of
    # 1 to 400 characters, not only white space. A failing entry is
    # never judged, so the program refuses to write one.
    if not 1 <= len(text) <= 400:
        raise ValueError(f"rant is {len(text)} characters, must be 1-400")
    if not text.strip():
        raise ValueError("rant must not be only whitespace")
    text.encode("utf-8")


def main() -> None:
    check(RANT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(RANT, encoding="utf-8")
    print(f"wrote {len(RANT)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
