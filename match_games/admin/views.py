import jwt
from flask import Blueprint, current_app, request

from match_games import bcrypt
from match_games.decorators import json, transational
from match_games.models import Role, User

blueprint = Blueprint('admin', __name__)


@blueprint.route('/admin/authentication', methods=['POST'])
@transational()
@json()
def authentication():
    user = (User.query
            .filter(User.email == request.json['email'], Role.name == 'admin')
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
