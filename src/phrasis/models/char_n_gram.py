from collections import Counter

from phrasis.models.base import BaseModel


class CharacterLanguageModel(BaseModel):
    def __init__(self, n: int = 5):
        self.n = n
        self.counts = Counter()
        self.total = 0
        self.model = {}

    def train(self, corpus: list[str]) -> None:
        self.counts.clear()
        self.total = 0

        for text in corpus:
            padded = f"{'~' * (self.n - 1)}{text.lower()}{'~' * (self.n - 1)}"

            for i in range(len(padded) - self.n + 1):
                gram = padded[i : i + self.n]
                self.counts[gram] += 1
                self.total += 1

        for gram, count in self.counts.items():
            self.model[gram] = count / self.total

    def score(self, text: str) -> float:
        if not self.model:
            raise ValueError("Model not trained")

        padded = f"{'~' * (self.n - 1)}{text.lower()}{'~' * (self.n - 1)}"

        scores = []
        for i in range(len(padded) - self.n + 1):
            gram = padded[i : i + self.n]
            prob = self.model.get(gram, 1e-9)
            scores.append(prob)

        return sum(scores) / len(scores)
