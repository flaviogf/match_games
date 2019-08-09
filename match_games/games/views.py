from flask import Blueprint

blueprint = Blueprint('games', __name__)


@blueprint.route('/games')
def games():
    return 'OK'
