import pytest
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists


db_uri = 'postgresql://postgres:edison@127.0.0.1/edison'

@pytest.fixture(scope="module")
def engine():
    return create_engine(db_uri)

def test_db_exist():
    assert database_exists(db_uri) is True

def test_db_connection(engine):
    assert engine.connect() is not None

def test_db_tables_exist(engine):
    tables = sqlalchemy.inspect(engine).get_table_names()
    assert 'users' in tables
