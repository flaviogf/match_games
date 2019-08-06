import pytest

from match_games import create_app


def app():
    app = create_app('config.Testing')

    with app.app_context():
        yield app
