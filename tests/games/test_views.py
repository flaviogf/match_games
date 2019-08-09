from match_games.models import Game


class TestGames:
    def test_should_return_status_201_when_game_is_created(self, client, image):
        data = {
            'name': "Pokemon Let's Go",
            'image': image
        }

        response = client.post('/games',
                               data=data,
                               content_type='multipart/form-data')

        assert 201 == response.status_code

    def test_should_insert_game_in_database(self, client, image):
        data = {
            'name': "Pokemon Let's Go",
            'image': image
        }

        response = client.post('/games',
                               data=data,
                               content_type='multipart/form-data')

        assert 1 == Game.query.count()
