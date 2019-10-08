import flask_sqlalchemy
from flask_login import UserMixin

db = flask_sqlalchemy.SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.username}'
