import threading
from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list):
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        email = EmailMessage(self.subject, self.body, self.from_email, self.recipient_list)
        email.send()
