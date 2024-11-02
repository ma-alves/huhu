from datetime import datetime
from typing import Dict, List

from tinydb.table import Document

from huhu.database import DatabaseHandler
from huhu import HUMOR


class HuhuController:
    def __init__(self, database) -> None:
        self._db_handler = DatabaseHandler(database).get_db()

    def add_record(self, humor: int, description: List[str] | None) -> Dict:
        if not description:
            description = ["No", "description."]

        description_text = " ".join(description).capitalize()
        if not description_text.endswith("."):
            description_text += "."

        record = {
            "humor": HUMOR.get(humor),
            "description": description_text,
            "datetime": datetime.now().strftime("%H:%M:%S, %d/%m/%Y"),
        }

        self._db_handler.insert(record)

        return record

    def read_record_by_id(self, id: int) -> Document:
        return self._db_handler.get(doc_id=id)

    def read_records(self) -> List[Document]:
        return self._db_handler.all()

    # ToDo: definir o que mudar por option: -h: humor -d: descrição -t: datetime
    def update_record(self) -> Document: ...

    def remove_record(self, id: int) -> str:
        return self._db_handler.remove(doc_ids=[id])
