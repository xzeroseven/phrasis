from phrasis.detectors.base import BaseDetector
from phrasis.models.char_n_gram import CharacterLanguageModel


class GibberishDetector(BaseDetector):
    def __init__(self, model: CharacterLanguageModel | None = None):
        self.model = model or CharacterLanguageModel()
        self.threshold = 0.002

    def analyze(self, text: str) -> dict:
        score = self.model.score(text)

        is_gibberish = score < self.threshold

        confidence = min(1.0, max(0.0, 1 - (score / self.threshold)))

        return {
            "text": text,
            "score": score,
            "label": "gibberish" if is_gibberish else "valid",
            "confidence": confidence,
        }
