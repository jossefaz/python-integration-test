import pytest

from app.db.metadata import Items
from app.service import items

@pytest.mark.integration
def test_create_item_creates_new_row_in_the_db(db_session) :
    """
    This test will call the create_item function from the item service and will assert that this call
    insert a new row in the database
    Arguments:
        db_session : a fixture that provide an open database session. It will helps us to retrieve row and assert
        that a new row was inserted
    """
    name = "John Doe"
    items.create_item(name)
    retrieved_item = db_session.query(Items).filter_by(id=1).first()
    assert retrieved_item.name == name
    assert retrieved_item.id == 1