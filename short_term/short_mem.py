from long_term.long_mem import LongTermMemory
from memory import Memory
from collections import deque

class ShortTermMemory(Memory):
    def __init__(self, capacity: int = 100, LongTermMemory: LongTermMemory = None):
        self.capacity = capacity
        self.short_term_memory = {}
        self.addition_timeline = deque()
        self.long_term_memory = LongTermMemory

    def add(self, key: str, value: str) -> bool:
        if len(self.short_term_memory) < self.capacity:
            self.short_term_memory[key] = value
            self.addition_timeline.append(key)
            return True
        else:
            last_item = self.addition_timeline.popleft()  # Remove the oldest entry
            del self.short_term_memory[last_item]
            self.long_term_memory.add(last_item, self.short_term_memory[last_item])  # Move it to long-term memory
            return False

    def remove(self, key: str) -> bool:
        if key in self.short_term_memory:
            del self.short_term_memory[key]
            self.addition_timeline.remove(key)
            return True
        return False

    def get(self, key: str) -> str:
        return self.short_term_memory.get(key)

    def modify(self, key: str, value: str) -> bool:
        if key in self.short_term_memory:
            self.short_term_memory[key] = value
            return True
        return False