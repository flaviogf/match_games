from flask import Blueprint

from match_games.decorators import transational, json
from match_games.models import Store, Game, User

blueprint = Blueprint('stats', __name__)


@blueprint.route('/api/v1/stats', methods=['GET'])
@transational()
@json()
def stats():
    data = {
        'games': Game.query.count(),
        'stores': Store.query.count(),
        'users': User.query.count()
    }

    return {'data': data, 'errors': []}, 200
