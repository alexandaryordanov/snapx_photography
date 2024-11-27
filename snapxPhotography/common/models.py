from django.contrib.auth import get_user_model
from django.db import models

from snapxPhotography.photos.models import Photo

# Create your models here.

UserModel = get_user_model()


class Vote(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='votes')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'photo')

    def __str__(self):
        return f'{self.user} voted on {self.photo.title}'
