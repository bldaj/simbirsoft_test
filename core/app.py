from core import create_app
from core.models import Cats, db

app = create_app()


@app.route('/')
def hello_world():
    c = Cats(name='cat example')
    db.session.add(c)
    db.session.commit()
    print(Cats.query.all())
    return '{}'.format(Cats.query.all())
