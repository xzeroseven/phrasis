from importlib import resources


def load():
    file = resources.files("phrasis.corpora").joinpath("data/zen_of_python/raw.txt")
    print(file)
    with open(file, encoding="utf-8") as f:
        text = f.read()
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    return lines
