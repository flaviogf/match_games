from os.path import dirname, join
from match_games.models import Store


class TestCreate:
    def test_should_access_create_return_status_200(self, client):
        response = client.get('/admin/store/create')

        assert 200 == response.status_code

    def test_should_return_field_required_when_name_not_is_informed(self, client):
        test_path = dirname(dirname(__file__))

        image_path = join(test_path, 'fixtures', 'default.png')

        with open(image_path, 'rb') as image:
            data = {
                'name': '',
                'image': image
            }

            response = client.post('/admin/store/create',
                                   data=data,
                                   content_type='multipart/form-data')

            assert b'This field is required.' in response.data

    def test_should_database_contains_one_store_when_store_is_created(self, client):
        test_path = dirname(dirname(__file__))

        image_path = join(test_path, 'fixtures', 'default.png')

        with open(image_path, 'rb') as image:
            data = {
                'name': 'ShopB',
                'image': image
            }

            client.post('/admin/store/create',
                        data=data,
                        content_type='multipart/form-data')

            assert 1 == Store.query.count()
