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
