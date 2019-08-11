from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
cors = CORS()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    from match_games import authentication
    app.register_blueprint(authentication.views.blueprint)
    from match_games import games
    app.register_blueprint(games.views.blueprint)

    from match_games import commands
    app.cli.add_command(commands.create_admin)

    return app
