from phrasis.corpora.registry import CORPORA


def load_builtin(name: str):
    if name not in CORPORA:
        raise ValueError(f"Unknown corpus: {name}")

    return CORPORA[name]()
