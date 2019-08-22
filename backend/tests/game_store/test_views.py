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

    def test_should_return_400_when_game_store_with_game_id_and_store_id_already_exists(self, client, db, game, store, game_store):
        db.session.add(game)
        db.session.add(store)
        db.session.add(game_store)

        db.session.commit()

        data = {
            'game_id': 1,
            'store_id': 1,
            'value': 199.99
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


class TestSingle:
    def test_should_return_status_200_when_game_store_exists(self, client, db, game, store, game_store):
        db.session.add(game)
        db.session.add(store)
        db.session.add(game_store)

        db.session.commit()

        response = client.get('/api/v1/game-store/1')

        assert 200 == response.status_code

    def test_should_return_status_404_when_game_store_not_exists(self, client):
        response = client.get('/api/v1/game-store/1')

        assert 404 == response.status_code


class TestUpdate:
    def test_should_return_status_200_when_update_game_store(self, client, db, game, store, game_store):
        db.session.add(game)
        db.session.add(store)
        db.session.add(game_store)

        db.session.commit()

        data = {
            'game_id': 1,
            'store_id': 1,
            'value': 199.99
        }

        response = client.put('/api/v1/game-store/1', json=data)

        assert 200 == response.status_code

    def test_should_return_status_404_when_game_store_not_exists(self, client):
        data = {
            'game_id': 1,
            'store_id': 1,
            'value': 199.99
        }

        response = client.put('/api/v1/game-store/1', json=data)

        assert 404 == response.status_code

    def test_should_update_database_when_game_store_is_updated(self, client, db, game, store, game_store):
        db.session.add(game)
        db.session.add(game)
        db.session.add(store)
        db.session.add(store)
        db.session.add(game_store)

        db.session.commit()

        data = {
            'game_id': 2,
            'store_id': 2,
            'value': 299.99
        }

        client.put('/api/v1/game-store/1', json=data)

        game_store = GameStore.query.first()

        result = {
            'game_id': game_store.game_id,
            'store_id': game_store.store_id,
            'value': game_store.value
        }

        assert data == result


@pytest.fixture
def game():
    return Game(name='Fifa 19', image='default.jpg')


@pytest.fixture
def store():
    return Store(name='Big Boy', image='default.jpg')


@pytest.fixture
def game_store():
    return GameStore(game_id=1, store_id=1, value=199.99)
