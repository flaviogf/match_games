import jwt
from flask import Blueprint, current_app, request

from match_games import bcrypt
from match_games.decorators import json
from match_games.models import User

blueprint = Blueprint('admin', __name__)


@blueprint.route('/admin/authentication', methods=['POST'])
@json()
def authentication():
    user = (User.query
            .filter_by(email=request.json['email'])
            .first())

    if not user or not bcrypt.check_password_hash(user.password, request.json['password']):
        return {'data': None, 'errors': ['Email or password invalid.']}, 401

    payload = {'id': user.id}

    secret_key = current_app.config.get('SECRET_KEY')

    algorithm = 'HS256'

    token = jwt.encode(payload, secret_key, algorithm).decode('utf-8')

    data = {
        'id': user.id,
        'name': user.name,
        'role': user.role.name,
        'token': token
    }

    return {'data': data, 'errors': []}, 200
