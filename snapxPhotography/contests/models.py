from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from snapxPhotography.categories.models import Category
from snapxPhotography.contests.validators import DateValidator

# Create your models here.

UserModel = get_user_model()


class Contest(models.Model):

    @property
    def is_open(self):
        return self.deadline > timezone.now().date()

    @property
    def participants(self):
        users = []

        for photo in self.photo.all():
            users.append(photo.uploaded_by)
        return len(set(users))

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Name'
    )

    requirements = models.TextField(
        max_length=255,
        verbose_name='Requirements',
        help_text='Please write down what requirements this contest should have'
    )

    award = models.PositiveIntegerField(
        help_text="Prize amount in currency (e.g., USD), maximum 5 digits",
        verbose_name="Award",
        validators=[
            MaxValueValidator(9999, message='Please enter a 4 digit number!!!'),
            MinValueValidator(1000, message='Please enter a 4 digit number!!!')
        ]
    )

    deadline = models.DateField(
        help_text="Deadline for contest submissions",
        verbose_name="Deadline Date",
        validators=[DateValidator()]
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='contest',
        verbose_name='Category',
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='contests'
    )

    def __str__(self):
        return self.name
