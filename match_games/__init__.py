from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from match_games import admin
    app.register_blueprint(admin.views.blueprint)
    from match_games import store
    app.register_blueprint(store.views.blueprint)

    return app
