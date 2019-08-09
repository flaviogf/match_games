from time import time

from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    from match_games import admin
    app.register_blueprint(admin.views.blueprint)

    return app
