import pytest

from match_games.models import Game


class TestCreate:
    def test_should_return_status_201_when_create_a_game(self, client, image):
        data = {
            'name': "Pokemon Let's Go Pikachu",
            'image': image
        }

        response = client.post('/api/v1/games',
                               data=data,
                               content_type='multipart/form-data')

        assert 201 == response.status_code

    def test_should_insert_game_in_database_when_create_a_game(self, client, image):
        data = {
            'name': "Pokemon Let's Go Pikachu",
            'image': image
        }

        client.post('/api/v1/games',
                    data=data,
                    content_type='multipart/form-data')

        assert 1 == Game.query.count()

    def test_should_return_status_400_when_name_not_is_informed(self, client, image):
        data = {
            'name': "",
            'image': image
        }

        response = client.post('/api/v1/games',
                               data=data,
                               content_type='multipart/form-data')

        assert 400 == response.status_code


class TestAll:
    def test_should_return_status_200(self, client, games):
        response = client.get('/api/v1/games?page=2')

        assert 200 == response.status_code

    def test_should_return_a_game_list(self, client, games):
        response = client.get('/api/v1/games?page=2')

        games = response.json['data']

        assert isinstance(games, list)

    def test_should_return_ten_games_per_request(self, client, games):
        response = client.get('/api/v1/games?page=2')

        games = response.json['data']

        assert 10 == len(games)

    def test_should_return_last_ten_games_when_requested_page_2(self, client, games):
        response = client.get('/api/v1/games?page=2')

        games = response.json['data']

        last_game = games[-1]

        assert 10 == last_game['id']

    @pytest.fixture
    def games(self, db):
        for index in range(20):
            game = Game(name=f'Game-{index}')
            db.session.add(game)

        db.session.commit()


class TestSingle:
    def test_should_return_status_200_when_game_exists(self, client, game):
        response = client.get(f'/api/v1/games/{game.id}')

        assert 200 == response.status_code

    def test_should_return_status_404_when_game_not_exists(self, client):
        response = client.get(f'/api/v1/games/1')

        assert 404 == response.status_code

    def test_should_return_the_game_when_it_exists(self, client, game):
        response = client.get(f'/api/v1/games/{game.id}')

        game = response.json['data']

        expected = {
            'id': 1,
            'name': "Pokemon Let's Go Pikachu",
            'image': 'default.jpg'
        }

        assert expected == game

    @pytest.fixture
    def game(self, db):
        db.session.add(Game(name="Pokemon Let's Go Pikachu"))
        db.session.commit()
        return Game.query.first()


class TestUpdate:
    def test_should_return_status_200_when_game_is_updated(self, client, game, image):
        data = {
            'name': 'xpto',
            'image': image
        }

        response = client.put(f'/api/v1/games/{game.id}',
                              data=data,
                              content_type='multipart/form-data')

        assert 200 == response.status_code

    def test_should_return_status_400_when_name_not_is_informed(self, client, game, image):
        data = {
            'name': '',
            'image': image
        }

        response = client.put(f'/api/v1/games/{game.id}',
                              data=data,
                              content_type='multipart/form-data')

        assert 400 == response.status_code

    def test_should_return_status_200_when_game_is_updated_without_a_new_image(self, client, game):
        data = {
            'name': 'xpto'
        }

        response = client.put(f'/api/v1/games/{game.id}',
                              data=data,
                              content_type='multipart/form-data')

        assert 200 == response.status_code

    def test_should_return_status_404_when_game_not_exists(self, client, image):
        data = {
            'name': "Pokemon Let's Go Eevee",
            'image': image
        }

        response = client.put('/api/v1/games/1',
                              data=data,
                              content_type='multipart/form-data')

        assert 404 == response.status_code

    @pytest.fixture
    def game(self, db):
        db.session.add(Game(name="Pokemon Let's Go Pikachu"))
        db.session.commit()
        return Game.query.first()
