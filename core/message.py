from flask import Blueprint, render_template
from flask_login import login_required

from core import redis_client
from core.config import REDIS_MESSAGE_TTL
from core.forms import SendForm

bp = Blueprint('message', __name__, url_prefix='/message')


@bp.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    form = SendForm()
    if form.validate_on_submit():
        redis_client.set('messages', form.message.data, ex=REDIS_MESSAGE_TTL)
        print('message: ', redis_client.get('messages'))
    return render_template('message/send.html', title='Send Message', form=form)
