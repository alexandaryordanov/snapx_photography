from asgiref.sync import sync_to_async
from django.core.mail import send_mail


async def send_email_async(subject, message, recipient_list, from_email='anonimovbg@gmail.com'):
    await sync_to_async(send_mail)(
        subject, message, from_email, recipient_list
    )
