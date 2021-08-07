from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

Items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
)