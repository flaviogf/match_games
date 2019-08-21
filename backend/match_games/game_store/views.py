from flask import Blueprint

blueprint = Blueprint('game_store', __name__)


@blueprint.route('/api/v1/game-store', methods=['POST'])
def create():
    return 'OK'
