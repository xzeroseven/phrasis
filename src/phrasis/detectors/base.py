from abc import ABC, abstractmethod


class BaseDetector(ABC):
    @abstractmethod
    def analyze(self, text: str) -> dict:
        pass
