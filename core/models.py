import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Cats(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.name}'
