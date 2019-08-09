from os import path

import pytest

from match_games import bcrypt as _bcrypt
from match_games import create_app
from match_games import db as _db


@pytest.yield_fixture
def app():
    app = create_app(config='config.Testing')

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    return _db


@pytest.fixture
def bcrypt(app):
    return _bcrypt


@pytest.yield_fixture
def image(app):
    image_path = path.join(path.dirname(__file__), 'fixtures', 'default.png')

    with open(image_path, 'rb') as image:
        yield image
