import functools


def transational():
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            from match_games import db
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
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            from flask import jsonify
            body, status = fn(*args, **kwargs)
            return jsonify(body), status
        return wrapper
    return decorator


def upload():
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            from os import path
            from flask import request, current_app
            image_name, status = fn(*args, **kwargs)
            upload_folder = current_app.config.get('UPLOAD_FOLDER')
            image = request.files['image']
            image_path = path.join(upload_folder, image_name)
            image.save(image_path)
            return image_name, status
        return wrapper
    return decorator
