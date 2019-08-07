import pytest

from match_games import create_app


@pytest.yield_fixture
def app():
    app = create_app('config.Testing')

    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()
