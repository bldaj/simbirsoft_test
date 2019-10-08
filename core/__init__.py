from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_redis import FlaskRedis

from core.config import REDIS_URL, SQLALCHEMY_DATABASE_URI
from core.models import db

login_manager = LoginManager()
redis_client = FlaskRedis()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['REDIS_URL'] = REDIS_URL
    app.config['SECRET_KEY'] = '123'
    app.app_context().push()

    db.init_app(app)
    db.create_all()

    redis_client.init_app(app)

    login_manager.init_app(app)
    Bootstrap(app)

    from core import auth
    app.register_blueprint(auth.bp)

    from core import message
    app.register_blueprint(message.bp)

    return app
