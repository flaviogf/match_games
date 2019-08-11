from os.path import dirname, join

import jwt
import pytest

from match_games import bcrypt as _bcrypt
from match_games import create_app
from match_games import db as _db
from match_games.models import User


@pytest.yield_fixture
def app():
    app = create_app(config='match_games.config.Testing')
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


@pytest.fixture
def admin(db, bcrypt):
    password_hash = bcrypt.generate_password_hash('xpto').decode('utf-8')
    db.session.add(User(name='barry',
                        email='flash@dc.com',
                        password=password_hash,
                        role='admin'))
    db.session.commit()


@pytest.fixture
def token(app, admin):
    payload = {
        'name': admin.name,
        'email': admin.email,
        'role': admin.role,
        'iss': 'match_games:backend',
        'aud': 'match_games:frontend'
    }

    secret = app.config.get('SECRET_KEY')

    token = jwt.encode(payload, secret, 'HS256').decode('utf-8')

    return token


@pytest.yield_fixture
def image(app):
    image_path = join(dirname(__file__), 'fixtures', 'image.jpg')

    with open(image_path, 'rb') as image:
        yield image
