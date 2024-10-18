import threading
import logging
from firebmail import sendmail, BatchMail
from django.template.loader import render_to_string
from django.utils.timezone import now
from django.conf import settings



def send_email(payload, recipient, context):
    """
    Send email to the recipient
    """
    try:
        mail_args = {
            'payload': render_to_string(payload, context),
            'subject': 'Email Verification',
            'sender': settings.APP_EMAIL,
            'password': settings.APP_PASSWORD,
            'recipient': recipient,
            'sender_name': 'Rcf-Funaab',
            'type_' : 'html'
        }
        threading.Thread(target=sendmail, kwargs=mail_args).start()
    except Exception as e:
        logging.error(str(e.with_traceback(None)))