from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def score(self, text: str) -> float:
        pass
