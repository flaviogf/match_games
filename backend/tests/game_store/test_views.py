import pytest

from match_games.models import Game, Store


class TestCreate:
    def test_should_return_status_200_when_create_game_store(self, client, db, game, store):
        db.session.add(game)
        db.session.add(store)
        db.session.commit()

        data = {
            'game_id': game.id,
            'store_id': store.id,
            'value': 199.99
        }

        response = client.post('/api/v1/game-store', json=data)

        assert 200 == response.status_code

    @pytest.fixture
    def game(self):
        return Game(name='Fifa 19', image='default.jpg')

    @pytest.fixture
    def store(self):
        return Store(name='Big Boy', image='default.jpg')
