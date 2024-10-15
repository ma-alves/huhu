# Alterar erros para algo mais padronizado

from datetime import datetime
from typing import List

from tinydb.table import Document

from database import DatabaseHandler
from huhu import HUMOR


class HuhuController:
    def __init__(self) -> None:
        self._db_handler = DatabaseHandler('database.json').get_db()


    def add_record(self, humor: int, description: List[str] | None = None):
        if not description:
            description_text = ['No', 'description.']

        description_text = ' '.join(description_text)
        if not description_text.endswith('.'):
            description_text += '.'

        if not isinstance(humor, int):
            print('Invalid type.')
            return 0

        record = {
            'humor': HUMOR.get(humor),
            'description': description_text,
            'datetime': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }

        try:
            self._db_handler.insert(record)
        except Exception as e:
            print(e)


    def read_record_by_id(self, id: int) -> Document:
        record = self._db_handler.get(doc_id=id)
        if not record:
            print('Record not found.')
            return 0
        return record


    def read_records(self) -> List[Document]:
        records = self._db_handler.all()
        if not records:
            print('No records found in the database.')
            return 0
        return records
