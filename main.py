"""The One-Liner Groan-Off — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the Wi-Fi gives the silent treatment, and the punchline turns on "space" — signal space and personal space.
TEXT = "I told my Wi-Fi it was acting up, so it gave me the silent treatment — turns out even the router needs space."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
