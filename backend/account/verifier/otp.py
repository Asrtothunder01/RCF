import pyotp 

from ..models import User, OTP

from church.utils.emailhandler import send_email


def create_otp(user, template):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    otp = totp.now()
    otp_object = OTP.objects.create(created_for=user, otp=otp)
    send_email(template, user.email, {'otp': otp_object.otp})
    return True