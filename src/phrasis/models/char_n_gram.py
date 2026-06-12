import math

from collections import Counter

from phrasis.models.base import BaseModel


class CharacterLanguageModel(BaseModel):
    def __init__(self, n: int = 3):
        self.n = n
        self.counts = Counter()
        self.total = 0
        self.model = {}

    def train(self, corpus: list[str]) -> None:
        self.counts.clear()
        self.total = 0

        for text in corpus:
            padded = f"{'~' * (self.n - 1)}{text.lower()}{'~' * (self.n - 1)}"

            num_grams = len(padded) - self.n + 1
            for i in range(num_grams):
                gram = padded[i : i + self.n]
                self.counts[gram] += 1
                self.total += 1

        for gram, count in self.counts.items():
            self.model[gram] = count / self.total

    def score(self, text: str) -> float:
        if not self.model:
            raise ValueError("Model not trained")

        padded = f"{'~' * (self.n - 1)}{text.lower()}{'~' * (self.n - 1)}"

        total_log_score = 0.0
        num_grams = len(padded) - self.n + 1
        for i in range(num_grams):
            gram = padded[i : i + self.n]
            prob = self.model.get(gram, 1e-9)
            total_log_score += math.log(prob)
        return total_log_score / num_grams
