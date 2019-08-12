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

        assert 20 == last_game['id']

    @pytest.fixture
    def games(self, db):
        for index in range(20):
            game = Game(name=f'Game-{index}')
            db.session.add(game)

        db.session.commit()
