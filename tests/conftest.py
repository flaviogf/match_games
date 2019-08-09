import pytest

from match_games import create_app
from match_games import db as _db


@pytest.yield_fixture
def app():
    app = create_app()

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
