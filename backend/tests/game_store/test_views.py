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


class TestAll:
    def test_should_return_status_200(self, client, db, game):
        for _ in range(20):
            db.session.add(game)

        db.session.commit()

        response = client.get('/api/v1/game-store')

        assert 200 == response.status_code

    def test_should_return_list_of_game_store(self, client, db, game):
        for _ in range(20):
            db.session.add(game)

        db.session.commit()

        response = client.get('/api/v1/game-store')

        list_game_store = response.json['data']

        assert isinstance(list_game_store, list)


@pytest.fixture
def game():
    return Game(name='Fifa 19', image='default.jpg')


@pytest.fixture
def store():
    return Store(name='Big Boy', image='default.jpg')
