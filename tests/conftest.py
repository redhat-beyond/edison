import pytest
import psycopg2


@pytest.fixture
def db_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="edison",
        user="postgres",
        password="edison")
    
    yield connection
    connection.close()

@pytest.fixture
def cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    db_connection.rollback()

@pytest.fixture
def build_users_table(cursor):
    cursor.execute("""
    INSERT INTO users (username) VALUES (%s);
    """,
    ("ahinoam",))

@pytest.fixture
def reset_users_primary_key(cursor):
    cursor.execute("""
    ALTER SEQUENCE users_id_seq RESTART;
    """)
