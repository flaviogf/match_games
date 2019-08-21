import pytest

from match_games.models import Game, GameStore, Store


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

    def test_should_update_database_when_create_game_store(self, client, db, game, store):
        db.session.add(game)
        db.session.add(store)
        db.session.commit()

        data = {
            'game_id': game.id,
            'store_id': store.id,
            'value': 199.99
        }

        response = client.post('/api/v1/game-store', json=data)

        assert 1 == GameStore.query.count()

    def test_should_return_status_400_when_game_id_not_is_informed(self, client):
        data = {
            'game_id': None,
            'store_id': 1,
            'value': 199.99
        }

        response = client.post('/api/v1/game-store', json=data)

        assert 400 == response.status_code

    def test_should_return_status_400_when_store_id_not_is_informed(self, client):
        data = {
            'game_id': 1,
            'store_id': None,
            'value': 199.99
        }

        response = client.post('/api/v1/game-store', json=data)

        assert 400 == response.status_code

    def test_should_return_status_400_when_value_not_is_informed(self, client):
        data = {
            'game_id': 1,
            'store_id': 1,
            'value': None
        }

        response = client.post('/api/v1/game-store', json=data)

        assert 400 == response.status_code

    @pytest.fixture
    def game(self):
        return Game(name='Fifa 19', image='default.jpg')

    @pytest.fixture
    def store(self):
        return Store(name='Big Boy', image='default.jpg')
