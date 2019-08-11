import jwt
from flask import Blueprint, current_app, jsonify, request

from match_games import bcrypt
from match_games.authentication.serializers import authentication_serializer
from match_games.decorators import json, validate
from match_games.models import User

blueprint = Blueprint('authentication', __name__)


@blueprint.route('/api/v1/authentication', methods=['POST'])
@validate(authentication_serializer)
@json()
def authentication():
    body = request.get_json(force=True)

    user = User.query.filter(User.email == body.get('email')).first()

    if user and bcrypt.check_password_hash(user.password, body.get('password')):
        payload = {
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'iss': 'match_games:backend',
            'aud': 'match_games:frontend'
        }

        secret = current_app.config.get('SECRET_KEY')

        token = jwt.encode(payload, secret, 'HS256').decode('utf-8')

        data = {
            'name': user.name,
            'email': user.email,
            'image': user.image,
            'token': token
        }

        return {'data': data, 'errors': []}, 200

    return {'data': None, 'errors': ['Email or password invalid']}, 401
