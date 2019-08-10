class TestAuthentication:
    def test_post_return_status_200_when_user_is_authenticated(self, client, admin):
        data = {
            'email': 'flash@dc.com',
            'password': 'xpto'
        }

        response = client.post('/api/v1/admin/authentication', json=data)

        assert 200 == response.status_code

    def test_post_return_status_401_when_user_not_is_authenticated(self, client):
        data = {
            'email': 'flash@dc.com',
            'password': 'wrong'
        }

        response = client.post('/api/v1/admin/authentication', json=data)

        assert 401 == response.status_code

    def test_should_return_status_400_when_email_is_empty(self, client):
        data = {
            'email': '',
            'password': 'xpto'
        }

        response = client.post('/api/v1/admin/authentication', json=data)

        assert 400 == response.status_code

    def test_should_return_status_400_when_password_is_empty(self, client):
        data = {
            'email': 'flash@dc.com',
            'password': ''
        }

        response = client.post('/api/v1/admin/authentication', json=data)

        assert 400 == response.status_code
