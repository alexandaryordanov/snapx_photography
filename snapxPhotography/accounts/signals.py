from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from snapxPhotography.accounts.models import Account

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
