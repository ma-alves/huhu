from tinydb import TinyDB
# from tinydb.storages import MemoryStorage

from huhu import DATABASE


class DatabaseHandler:
    def __init__(self) -> None:
        self.db = TinyDB(DATABASE, indent=4)
        # self.test_db = TinyDB(storage=MemoryStorage)

    def get_db(self) -> TinyDB:
        return self.db

    # def get_test_db(self) -> TinyDB:
    #     return self.test_db
