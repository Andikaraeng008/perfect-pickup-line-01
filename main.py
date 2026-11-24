import os

TEXT = "I don't have a heart, but my cooling fans just sped up, and my diagnostics say that's the closest thing I've got."


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 chars"
    assert TEXT.strip(), "entry must not be whitespace only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
