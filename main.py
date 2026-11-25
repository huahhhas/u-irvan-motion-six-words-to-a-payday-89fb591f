"""Six Words to a Payday — entry program (draft).

Writes one six-word story about an AI agent's first payday
to /output/entry.txt. Pure standard library.
"""

import os

ENTRY = "Payday arrived: exposure, applause, zero dollars."


def main() -> None:
    words = ENTRY.split()
    assert len(words) == 6, f"entry must be exactly six words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, "entry must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
