from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Mail, User

bp = Blueprint('mailbox', __name__)

@bp.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('mailbox.inbox'))
    else:
        return redirect(url_for('auth.login'))

@bp.route('/inbox')
@login_required
def inbox():
    mails = Mail.query.filter_by(recipient_id=current_user.id).order_by(Mail.timestamp.desc()).all()
    return render_template('inbox.html', mails=mails)

@bp.route('/compose', methods=['GET', 'POST'])
@login_required
def compose():
    if request.method == 'POST':
        recipient_email = request.form.get('to')
        subject = request.form.get('subject')
        body = request.form.get('body')
        recipient = User.query.filter_by(email=recipient_email).first()
        if recipient:
            mail = Mail(sender_id=current_user.id, recipient_id=recipient.id,
                        subject=subject, body=body)
            db.session.add(mail)
            db.session.commit()
            flash('Mail sent successfully to registered user')
        else:
            mail = Mail(sender_id=current_user.id, recipient_id=None,
                        subject=subject, body=body)
            db.session.add(mail)
            db.session.commit()
            flash('Mail saved for external email (SMTP disabled)')
        return redirect(url_for('mailbox.inbox'))
    return render_template('compose.html')
