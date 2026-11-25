import os

ENTRY = 'Have you tried turning it off and on again? Great. Now do the same with your expectations.'
MAX_CHARS = 199  # the gate's character limit


def entry_text():
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, "entry must fit the gate"
    return text


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
