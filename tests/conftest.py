import pytest
from sqlalchemy.orm import scoped_session, sessionmaker

from app.db.db_engine import get_engine

from config.loader import Configuration
from testcontainers.mysql import MySqlContainer


@pytest.fixture(scope='session')
def db_engine(mysql_instance):
    """yields a SQLAlchemy engine which is suppressed after the test session"""

    engine = get_engine()
    yield engine

    engine.dispose()


@pytest.fixture(scope='session')
def db_session_factory(db_engine):
    """returns a SQLAlchemy scoped session factory"""
    return scoped_session(sessionmaker(bind=db_engine))


@pytest.fixture(scope='session')
def db_session(db_session_factory):
    """yields a SQLAlchemy connection which is rollbacked after the test"""
    session_ = db_session_factory()

    yield session_

    try:
        session_.rollback()
    except Exception:
        pass


@pytest.fixture(scope='session', autouse=True)
def mysql_instance():
    db_config = Configuration().get("db")
    with MySqlContainer(MYSQL_DATABASE=db_config.get('database')) as mysql:
        update_mysql_config(mysql) #<=== UPDATE THE DB CONFIG
        yield mysql


def update_mysql_config(mysql):
    db_config = Configuration().get("db")
    db_config['port'] = int(mysql.get_exposed_port(mysql.port_to_expose))
    db_config['username'] = mysql.MYSQL_USER
    db_config['password'] = mysql.MYSQL_PASSWORD
    db_config['database'] = mysql.MYSQL_DATABASE


@pytest.fixture
def client():
    from app.server import app
    return app
