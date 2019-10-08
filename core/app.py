from core import create_app, login_manager
from core.models import User

app = create_app()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
