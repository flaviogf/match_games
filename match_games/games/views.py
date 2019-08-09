import secrets

from flask import Blueprint, request

from match_games import db
from match_games.decorators import json, transational, upload
from match_games.models import Game

blueprint = Blueprint('games', __name__)


@blueprint.route('/games', methods=['POST'])
@transational()
@json()
@upload()
def index():
    image = f"{secrets.token_hex(8)}.jpg"

    game = Game(name=request.form['name'], image=image)

    db.session.add(game)

    return image, 201
