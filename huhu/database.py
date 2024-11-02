from tinydb import TinyDB


class DatabaseHandler:
    def __init__(self, file) -> None:
        self.db = TinyDB(file)

    def get_db(self) -> TinyDB:
        return self.db
