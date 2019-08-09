import functools


def json():
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwagrs):
            from flask import jsonify
            body, status = fn(*args, **kwagrs)
            return jsonify(body), status
        return wrapper
    return decorator
