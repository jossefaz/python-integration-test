from app.db.db_engine import engine
from app.db.metadata import metadata
from app.service.items import create_item


def setup_app():
    """
    In a real life you would have here some setup for your web app like
    app = FastAPI() or app = Flask()
    and those
    """
    metadata.create_all(engine)
    return "A good application constructor"


app = setup_app()

if __name__ == '__main__':
    setup_app()
    create_item("John Doe")
