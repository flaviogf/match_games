import pytest

from match_games.models import Store


class TestCreate:
    def test_should_return_status_201_when_store_is_created(self, client, image):
        data = {
            'name': 'ShopB',
            'image': image
        }

        response = client.post('/api/v1/stores',
                               data=data,
                               content_type='multipart/form-data')

        assert 201 == response.status_code

    def test_should_return_status_400_when_name_not_is_informed(self, client, image):
        data = {
            'name': '',
            'image': image
        }

        response = client.post('/api/v1/stores',
                               data=data,
                               content_type='multipart/form-data')

        assert 400 == response.status_code


class TestAll:
    def test_should_return_status_200(self, client, stores):
        response = client.get('/api/v1/stores?page=1')

        assert 200 == response.status_code

    def test_should_return_stores_list(self, client, stores):
        response = client.get('/api/v1/stores?page=1')

        stores = response.json['data']

        assert isinstance(stores, list)

    def test_should_return_first_page_when_page_not_is_informed(self, client, stores):
        response = client.get('/api/v1/stores?page=1')

        stores = response.json['data']

        last_store = stores[-1]

        assert 'Store 15' == last_store['name']

    def test_should_return_second_page_when_page_informed_is_equal_to_2(self, client, stores):
        response = client.get('/api/v1/stores?page=2')

        stores = response.json['data']

        last_store = stores[-1]

        assert 'Store 5' == last_store['name']

    @pytest.fixture
    def stores(self, db):
        for index in range(20):
            store = Store(name=f'Store {index}')
            db.session.add(store)

        db.session.commit()
