class TestGames:
    def test_should_return_status_200_when_list_games(self, client):
        response = client.get('/games')

        assert 200 == response.status_code
