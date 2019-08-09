class TestAuthentication:
    def test_should_access_authentication_return_status_200(self, client):
        response = client.get('/admin/authentication')

        assert 200 == response.status_code


class TestStores:
    def test_should_access_stores_return_status_200(self, client):
        response = client.get('/admin/stores')

        assert 200 == response.status_code


class TestGames:
    def test_should_access_games_return_status_200(self, client):
        response = client.get('/admin/games')

        assert 200 == response.status_code
