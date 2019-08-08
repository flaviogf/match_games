import secrets
from os.path import dirname, join

UPLOAD_PATH = join(dirname(__file__), 'static', 'uploads')


def upload(file):
    file_name_hash = secrets.token_hex()

    file_name = file_name_hash + '.jpg'

    file_path = join(UPLOAD_PATH, file_name)

    file.save(file_path)

    return file_name
