from memory import Memory, MemoryItem
import sqlite3

class LongTermMemory(Memory):
    def __init__(self):
        self.con = sqlite3.connect("robot_memory.db")
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                timestamp TEXT NOT NULL
                    
            )
        """)
        self.con.commit()


    def add(self, memory: MemoryItem) -> bool:
        pass


    