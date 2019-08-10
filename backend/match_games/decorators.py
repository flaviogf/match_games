from functools import wraps
from json import dumps

from flask import Response, request


def validate(serializer):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            errors = serializer.validate(request.json)

            errors = [field_error
                      for _, field_errors in errors.items()
                      for field_error in field_errors]

            if errors:
                return {'data': None, 'errors': errors}, 400

            return fn(*args, **kwargs)
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
