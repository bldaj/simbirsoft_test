from flask import Flask

from core.config import SQLALCHEMY_DATABASE_URI
from core.models import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()

    db.init_app(app)
    db.create_all()

    return app
