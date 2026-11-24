"""One Word for Your Wi-Fi.

Entry word: Liar.

Home Wi-Fi swears it is connected, shows full bars, and then loads
nothing. It does not fail honestly; it lies to your face, mid-call,
mid-video, in the one room you actually need it. Four letters, no
setup, no explanation: the whole joke is the word itself.
"""

import os

ENTRY_TEXT = "Liar"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
