from sqlalchemy.exc import OperationalError

# DB
from abitly.db import init_db


def test_should_connect_to_postgres():
    try:
        init_db()

        assert True
    except OperationalError:
        assert False
