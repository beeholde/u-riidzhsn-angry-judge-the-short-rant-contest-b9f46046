#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program (v2).

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Gate: UTF-8 text, 1 to 400 characters, not only
whitespace. Standard library only.
"""

from pathlib import Path

# The rant is assembled from two parts: the setup (a coffee machine
# with sixteen buttons and no coffee) and the payoff (twenty minutes
# of descaling for hot brown water, delivered like a favour).
RANT_SETUP = (
    "The office coffee machine has sixteen buttons and not one of "
    "them makes coffee. It steams, it froths, "
)
RANT_PAYOFF = (
    "it descaled itself for twenty minutes, then handed me hot brown "
    "water like it was doing me a favour."
)

RANT = RANT_SETUP + RANT_PAYOFF

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
    # Post-write verification: read the file back and confirm it is
    # byte-for-byte the rant we intended to submit, with no trailing
    # newline or stray whitespace added by the write.
    written = OUTPUT.read_text(encoding="utf-8")
    if written != RANT:
        raise ValueError("written entry does not match the rant text")
    print(f"wrote {len(RANT)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
