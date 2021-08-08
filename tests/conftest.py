import pytest
from sqlalchemy.orm import scoped_session, sessionmaker

from app.db.db_engine import engine

from sqlalchemy import create_engine

from app.app import app

@pytest.fixture(scope='session')
def db_engine(request):
    """yields a SQLAlchemy engine which is suppressed after the test session"""

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
        session_.close()
    except Exception:
        pass


@pytest.fixture
def client():
    return app