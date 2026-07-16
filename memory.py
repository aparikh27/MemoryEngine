from abc import ABC, abstractmethod

class Memory(ABC):
    @abstractmethod
    def add(self, key: str, value: str) -> None:
        pass
    def get(self, key: str) -> str:
        pass
    def delete(self, key: str) -> None:
        pass
    def modify(self, key: str, value: str) -> None:
        pass