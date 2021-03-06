from sqlalchemy.orm import Session
from app.db.db_engine import engine
from app.db.metadata import Items
from app.db.items import insert


def create_item(name: str):
    with Session(engine) as session:
        item_id = insert(name, session)
        session.commit()
    print(f"Item created with id {item_id}")
