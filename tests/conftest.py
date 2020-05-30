import pytest
import sys, os

# Making edison module visible from tests folder.
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

from edison.app import app

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client
