# app/db/db_engine.py

from sqlalchemy import create_engine

from config.loader import Configuration


def build_url():
    db_config = Configuration().get("db")
    return 'mysql+pymysql://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s' % db_config


def get_engine():
    return create_engine(build_url())
