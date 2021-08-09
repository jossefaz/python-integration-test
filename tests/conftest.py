import time

import pytest
from sqlalchemy.orm import scoped_session, sessionmaker

from app.db.db_engine import build_url

from sqlalchemy import create_engine

from config.loader import Configuration
from testcontainers.mysql import MySqlContainer


@pytest.fixture(scope='session')
def db_engine(request):
    """yields a SQLAlchemy engine which is suppressed after the test session"""
    engine_ = create_engine(build_url())

    yield engine_

    engine_.dispose()


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
        yield mysql


