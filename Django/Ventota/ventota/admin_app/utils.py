from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "This is a email from ventota"
    message = "Test message"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["pasanglsherpa231@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)