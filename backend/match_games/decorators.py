from functools import wraps
from json import dumps
from os.path import join

from flask import Response, current_app, request
from PIL import Image

from match_games import db


def transational():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                result = fn(*args, **kwargs)
                db.session.commit()
                return result
            except:
                db.session.rollback()
                raise
        return wrapper
    return decorator


def json():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            content, status_code = fn(*args, **kwargs)
            response = Response(content_type='application/json',
                                response=dumps(content),
                                status=status_code)
            return response
        return wrapper
    return decorator


def validate(serializer):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            errors = serializer.validate(request.json or request.form)

            errors = [field_error
                      for _, field_errors in errors.items()
                      for field_error in field_errors]

            if errors:
                return {'data': None, 'errors': errors}, 400

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def upload(field='image'):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            response, status = fn(*args, **kwargs)

            upload_dir = current_app.config.get('UPLOAD_DIR')
            image_path = join(upload_dir, response['data']['image'])

            image = Image.open(request.files[field])
            image.thumbnail((100, 100))
            image.save(image_path)

            return response, status
        return wrapper
    return decorator
