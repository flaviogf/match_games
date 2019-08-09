class TestStores:
    def test_should_return_status_200_when_list_store(self, client):
        response = client.get('/stores')

        assert 200 == response.status_code
