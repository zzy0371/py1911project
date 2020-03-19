from celery import Celery
from views import mail
from flask_mail import Message
from flask import current_app
celery_app = Celery(__name__,broker="redis://localhost:6379/1")

@celery_app.task
def send_mail_async(subject,email,html):
    with current_app.app_context():
        msg = Message(subject,recipients=[email])
        msg.html=html
        mail.send(msg)
