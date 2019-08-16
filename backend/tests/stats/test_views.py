class TestStats:
    def test_should_return_status_200(self, client):
        response = client.get('/api/v1/stats')

        assert 200 == response.status_code

    def test_should_return_games_count(self, client):
        response = client.get('/api/v1/stats')

        games = response.json['data']['games']

        assert isinstance(games, int)

    def test_should_return_stores_count(self, client):
        response = client.get('/api/v1/stats')

        stores = response.json['data']['stores']

        assert isinstance(stores, int)

    def test_should_return_users_count(self, client):
        response = client.get('/api/v1/stats')

        users = response.json['data']['users']

        assert isinstance(users, int)
