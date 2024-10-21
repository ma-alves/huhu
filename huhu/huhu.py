# Alterar erros para algo mais padronizado

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
            description = ['No', 'description.']

        description_text = ' '.join(description).capitalize()
        if not description_text.endswith('.'):
            description_text += '.'

        if not isinstance(humor, int):
            print('Invalid type.')
            return None

        record = {
            'humor': HUMOR.get(humor),
            'description': description_text,
            'datetime': datetime.now().strftime("%H:%M:%S, %d/%m/%Y")
        }

        try:
            self._db_handler.insert(record)
        except Exception as e:
            print(e) # Não roda
        else:
            return record


    def read_record_by_id(self, id: int) -> Document:
        record = self._db_handler.get(doc_id=id)
        if not record:
            print('Record not found.')
            return None
        return record


    def read_records(self) -> List[Document]:
        records = self._db_handler.all()
        if not records:
            print('No records found in the database.')
            return None
        return records


    def update_record(self) -> Document:
        ...


    def delete_record(self) -> str:
        ...