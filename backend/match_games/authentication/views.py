import re

import jwt
from flask import Blueprint, current_app, jsonify, request

from match_games import bcrypt
from match_games.authentication.serializers import authentication_serializer
from match_games.decorators import json, transational, validate
from match_games.models import User

blueprint = Blueprint('authentication', __name__)


@blueprint.route('/api/v1/authentication', methods=['POST'])
@validate(authentication_serializer)
@transational()
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


@blueprint.route('/api/v1/authentication/validate-token', methods=['POST'])
@transational()
@json()
def validate_token():
    token = request.headers.get('Authorization', '')

    token = re.sub(r'Bearer\s', '', token)

    secret = current_app.config.get('SECRET_KEY')

    try:
        jwt.decode(token,
                   key=secret,
                   issuer='match_games:backend',
                   audience='match_games:frontend',
                   algorithms=['HS256'])
    except jwt.DecodeError:
        return {'data': False, 'errors': []}, 401
    else:
        return {'data': True, 'errors': []}, 200
