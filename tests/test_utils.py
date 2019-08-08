from os.path import dirname, join

from werkzeug.datastructures import FileStorage

from match_games.utils import upload


class TestUpload:
    def test_should_return_image_uploaded_name(self):
        test_path = dirname(__file__)

        image_path = join(test_path, 'fixtures', 'default.png')

        with open(image_path, 'rb') as image:
            name = upload(FileStorage(image, filename='default.png'))

            assert isinstance(name, str)
