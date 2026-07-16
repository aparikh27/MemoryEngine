from abc import ABC, abstractmethod, dataclass

@dataclass
class MemoryItem:
    key: str
    value: str
    timestamp: float

class Memory(ABC):
    @abstractmethod
    def add(self, memory: MemoryItem) -> bool:
        pass
    @abstractmethod
    def get(self, memory: MemoryItem) -> str:
        pass
    @abstractmethod
    def delete(self, memory: MemoryItem) -> bool:
        pass
    @abstractmethod
    def modify(self, memory: MemoryItem) -> bool:
        pass