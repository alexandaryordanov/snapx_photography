from django.utils import timezone

from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Category(models.Model):

    class Meta:
        ordering = ['pk']

    @property
    def contests_open(self):
        return self.contest.filter(deadline__gt=timezone.now().date())

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name='Description')
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='categories')
    category_image = CloudinaryField(verbose_name='Category Image',)

    def __str__(self):
        return self.name
