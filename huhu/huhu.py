from datetime import datetime
from typing import Dict, List

from tinydb.table import Document

from huhu.database import DatabaseHandler
from huhu import HUMOR


class HuhuController:
    def __init__(self) -> None:
        self._db_handler = DatabaseHandler().get_db()

    def add_record(self, humor: int, description: List[str] | None) -> Dict:
        if not description:
            description = ["Sem", "descrição."]

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

    def read_record(self, id: int) -> Document:
        return self._db_handler.get(doc_id=id)

    def read_records(self) -> List[Document]:
        return self._db_handler.all()

    # ToDo: definir o que mudar por option: -h: humor -d: descrição
    # -t: datetime -> fodase por enquanto
    def update_record(
        self,
        id: int,
        humor: int | None = None,
        description: List[str] | None = None,
    ) -> ...:
        if humor:
            self._db_handler.update({"humor": HUMOR.get(humor)}, doc_ids=[id])

        if description:
            description_text = " ".join(description).capitalize()
            if not description_text.endswith("."):
                description_text += "."
            self._db_handler.update(
                {"description": description_text}, doc_ids=[id]
            )

        return self._db_handler.get(doc_id=id)

    def remove_record(self, id: int) -> str:
        return self._db_handler.remove(doc_ids=[id])

    def remove_all_records(self) -> str:
        self._db_handler.truncate()
