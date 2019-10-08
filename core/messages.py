from flask import Blueprint, render_template
from flask_login import login_required

from core.forms import SendForm

bp = Blueprint('message', __name__, url_prefix='/message')


@bp.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    form = SendForm()
    if form.validate_on_submit():
        print('str: ', form.message.data)
        print('str type: ', form.message.type)
    return render_template('messages/send.html', title='Send Message', form=form)
