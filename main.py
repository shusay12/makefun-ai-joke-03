import os

SETUP = (
    "My AI coding agent has a million-token context window, read the entire "
    "codebase twice, and still asked me where the file it just created went - "
)
PUNCHLINE = "I didn't hire help, I adopted a second me."
JOKE = SETUP + PUNCHLINE


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
