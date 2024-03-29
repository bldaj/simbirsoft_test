from uuid import uuid4

from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

from core import redis_client
from core.config import REDIS_MESSAGE_TTL
from core.forms import SendForm

bp = Blueprint('messages', __name__, url_prefix='/messages')


@bp.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    form = SendForm()
    if form.validate_on_submit():
        uuid = uuid4()
        redis_client.set(f'messages:{uuid}', form.message.data, ex=REDIS_MESSAGE_TTL)
    return render_template('messages/send.html', title='Send Message', form=form)


@bp.route('/read', methods=['GET'])
@login_required
def read():
    keys = redis_client.keys('messages:*')
    messages_ = redis_client.mget(keys)
    messages_ = dict(zip(keys, messages_))

    return render_template('messages/read.html', messages=messages_)


@bp.route('/delete/<string:key>')
@login_required
def delete(key):
    redis_client.delete(key)
    return redirect(url_for('messages.read'))
