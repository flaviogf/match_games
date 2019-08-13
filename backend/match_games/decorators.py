from functools import wraps
from json import dumps

from flask import Response, request

from match_games import db


def validate(serializer):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            errors = serializer.validate(request.json or request.form)

            errors = [field_error
                      for _, field_errors in errors.items()
                      for field_error in field_errors]

            if errors:
                content = {'data': None, 'errors': errors}
                response = Response(content_type='application/json',
                                    response=dumps(content),
                                    status=400)
                return response

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def transational():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                response = fn(*args, **kwargs)
                db.session.commit()
                return response
            except:
                db.session.rollback()
                raise
        return wrapper
    return decorator


def json():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            content, status_code, *options = fn(*args, **kwargs)
            headers = options[0] if options else {}
            response = Response(content_type='application/json',
                                headers=headers,
                                response=dumps(content),
                                status=status_code)

            return response
        return wrapper
    return decorator
