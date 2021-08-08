from app.db.metadata import Items


def insert(name, session):
    query = Items.insert().values(name=name)
    new_item_id = session.execute(query)
    return new_item_id.lastrowid
