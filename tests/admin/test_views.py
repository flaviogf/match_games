class TestAuthenticate:
    def test_should_access_authenticate_return_status_200(self, client):
        response = client.get('/admin')

        assert 200 == response.status_code

    def test_should_return_field_required_when_email_not_is_inform(self, client):
        data = {
            'email': '',
            'password': 'iris west'
        }

        response = client.post('/admin', data=data)

        assert b'This field is required.' in response.data

    def test_should_return_field_required_when_password_not_is_inform(self, client):
        data = {
            'email': 'flash@dc.com',
            'password': ''
        }

        response = client.post('/admin', data=data)

        assert b'This field is required.' in response.data
