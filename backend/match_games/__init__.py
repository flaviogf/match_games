from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from rq import Queue

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
cors = CORS()
q = Queue(connection=Redis())


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app, expose_headers='*')

    from match_games import authentication
    app.register_blueprint(authentication.views.blueprint)
    from match_games import games
    app.register_blueprint(games.views.blueprint)
    from match_games import stores
    app.register_blueprint(stores.views.blueprint)
    from match_games import stats
    app.register_blueprint(stats.views.blueprint)
    from match_games import game_store
    app.register_blueprint(game_store.views.blueprint)

    from match_games import commands
    app.cli.add_command(commands.create_admin)

    return app
