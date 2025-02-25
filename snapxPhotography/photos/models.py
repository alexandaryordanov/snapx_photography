from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from snapxPhotography.contests.models import Contest

# Create your models here.

UserModel = get_user_model()


class Photo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    image = CloudinaryField()
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='photo', verbose_name='Contest')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='photos')
    vote = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ['-vote', 'uploaded_at']

    def __str__(self):
        return self.title
