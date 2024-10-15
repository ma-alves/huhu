from datetime import datetime
from typing import NamedTuple

from tinydb import TinyDB

# Sem uso por enquanto
class HumorRecord(NamedTuple):
    id: int
    humor: str
    description: str
    time: datetime


class DatabaseHandler:
    def __init__(self, file) -> None:
        self.db = TinyDB(file)

    def get_db(self) -> TinyDB:
        return self.db