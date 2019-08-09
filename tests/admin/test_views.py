import pytest

from match_games.models import Role, User


class TestAuthentication:
    def test_should_return_status_200_when_admin_is_authenticated(self, client, barry):
        data = {
            'email': 'barry@dc.com',
            'password': 'test123'
        }

        response = client.post('/admin/authentication', json=data)

        assert 200 == response.status_code

    def test_should_return_status_401_when_password_is_wrong(self, client, barry):
        data = {
            'email': 'barry@dc.com',
            'password': 'wrong'
        }

        response = client.post('/admin/authentication', json=data)

        assert 401 == response.status_code

    def test_should_return_status_401_when_email_is_wrong(self, client):
        data = {
            'email': 'barry@dc.com',
            'password': 'test123'
        }

        response = client.post('/admin/authentication', json=data)

        assert 401 == response.status_code

    def test_should_return_token_when_admin_authenticated(self, client, barry):
        data = {
            'email': 'barry@dc.com',
            'password': 'test123'
        }

        response = client.post('/admin/authentication', json=data)

        assert response.json['data']['token']

    @pytest.fixture
    def admin_role(self, db):
        admin = Role(name='admin')
        db.session.add(admin)
        db.session.commit()
        return admin

    @pytest.fixture
    def barry(self, admin_role, db, bcrypt):
        password_hash = (bcrypt.generate_password_hash('test123')
                         .decode('utf-8'))
        barry = User(name='barry',
                     email='barry@dc.com',
                     password=password_hash,
                     role_id=admin_role.id)
        db.session.add(barry)
        db.session.commit()
        return barry
