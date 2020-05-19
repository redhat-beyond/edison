import pytest
import psycopg2


def test_users_table_rows_count(cursor, build_users_table):
    cursor.execute("""
    SELECT * FROM users;
    """)
    result = cursor.fetchall()
    assert len(result) == 1

def test_username(cursor, build_users_table):
    cursor.execute("""
    SELECT username FROM users;
    """)
    result = cursor.fetchone()
    assert result[0] == "ahinoam"
