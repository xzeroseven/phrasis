import math

from phrasis.detectors.base import BaseDetector

from phrasis.models.char_n_gram import CharacterLanguageModel


class GibberishDetector(BaseDetector):
    def __init__(
        self, model: CharacterLanguageModel | None = None, threshold: float = -6.5
    ):
        self.model = model or CharacterLanguageModel()
        self.threshold = threshold

    def analyze(self, text: str) -> dict:
        if not self.model:
            raise ValueError("Model not trained")

        score = self.model.score(text)
        is_gibberish = score < self.threshold
        worst_score = math.log(1e-9)

        if is_gibberish:
            distance = self.threshold - score
            max_possible_distance = self.threshold - worst_score
        else:
            distance = score - self.threshold
            max_possible_distance = 0.0 - self.threshold
        if max_possible_distance <= 0:
            confidence = 1.0
        else:
            confidence = min(1.0, max(0.0, distance / max_possible_distance))
        return {
            "text": text,
            "score": score,
            "label": "gibberish" if is_gibberish else "valid",
            "confidence": round(confidence, 6),
        }
