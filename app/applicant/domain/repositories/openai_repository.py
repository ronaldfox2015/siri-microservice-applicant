from abc import ABC, abstractmethod


class OpenaiRepository(ABC):
    @abstractmethod
    def search_by_prompt(self, prompt: str):
        pass