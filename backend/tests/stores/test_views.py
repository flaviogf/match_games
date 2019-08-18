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


class TestSingle:
    def test_should_return_status_200_when_store_exist(self, client, store):
        response = client.get(f'/api/v1/stores/{store.id}')

        assert 200 == response.status_code

    def test_should_return_status_404_when_store_not_exists(self, client):
        response = client.get('/api/v1/stores/1')

        assert 404 == response.status_code

    def test_should_return_the_store_when_it_exists(self, client, store):
        response = client.get(f'/api/v1/stores/{store.id}')

        expected = {
            'id': 1,
            'name': 'Store',
            'image': 'default.jpg',
            'image_path': 'http://localhost/static/uploads/default.jpg'
        }

        result = response.json['data']

        assert expected == result

    @pytest.fixture
    def store(self, db):
        store = Store(name='Store')
        db.session.add(store)
        db.session.commit()
        return store


class TestUpdate:
    def test_should_return_status_200_when_update_the_store(self, client, image, store):
        data = {
            'name': 'test',
            'image': image
        }

        response = client.put(f'/api/v1/stores/{store.id}',
                              data=data,
                              content_type='multipart/form-data')

        assert 200 == response.status_code

    def test_should_return_status_200_when_image_not_is_informed(self, client, store):
        data = {
            'name': 'Test'
        }

        response = client.put(f'/api/v1/stores/{store.id}',
                              data=data,
                              content_type='multipart/form-data')

        assert 200 == response.status_code

    def test_should_return_status_400_when_name_not_is_informed(self, client, image, store):
        data = {
            'name': '',
            'image': image
        }

        response = client.put(f'/api/v1/stores/{store.id}',
                              data=data,
                              content_type='multipart/form-data')

        assert 400 == response.status_code

    def test_should_return_status_404_when_store_not_exists(self, client, image):
        data = {
            'name': 'test',
            'image': image
        }

        response = client.put('/api/v1/stores/1',
                              data=data,
                              content_type='multipart/form-data')

        assert 404 == response.status_code

    @pytest.fixture
    def store(self, db):
        store = Store(name='Store')
        db.session.add(store)
        db.session.commit()
        return store


class TestDetroy:
    def test_should_return_status_200_when_store_is_deleted(self, client, store):
        response = client.delete(f'/api/v1/stores/{store.id}')

        assert 200 == response.status_code

    def test_should_return_status_404_when_store_not_exists(self, client):
        response = client.delete('/api/v1/stores/1')

        assert 404 == response.status_code

    @pytest.fixture
    def store(self, db):
        store = Store(name='XPTO')
        db.session.add(store)
        db.session.commit()
        return store
