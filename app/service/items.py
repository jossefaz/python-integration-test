from sqlalchemy.orm import Session
from app.db.db_engine import get_engine
from app.db.items import insert


def create_item(name: str):
    with Session(get_engine()) as session:
        item_id = insert(name, session)
        session.commit()
    return item_id
