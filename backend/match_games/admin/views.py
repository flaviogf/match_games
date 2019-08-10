from flask import Blueprint, jsonify, request

from match_games import bcrypt
from match_games.admin.serializers import authentication_serializer
from match_games.decorators import json, validate
from match_games.models import User

blueprint = Blueprint('admin', __name__)


@blueprint.route('/api/v1/admin/authentication', methods=['POST'])
@validate(authentication_serializer)
@json()
def authentication():
    body = request.get_json(force=True)

    user = User.query.filter(User.email == body.get('email')).first()

    if user and bcrypt.check_password_hash(user.password, body.get('password')):
        return {'data': 'OK', 'errors': []}, 200

    return {'data': None, 'errors': ['Email or password invalid']}, 401
