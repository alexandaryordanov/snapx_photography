from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary.models import CloudinaryField
from snapxPhotography.accounts.managers import MyAppUserManager
from snapxPhotography.accounts.validators import PhoneNumberValidator, NameValidator


# Create your models here.
class MyAppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, )
    email = models.EmailField(unique=True, )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAppUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


UserModel = get_user_model()


class Account(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 30
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=True,
        verbose_name="First Name",
        validators=[
            NameValidator(),
            MinLengthValidator(NAME_MIN_LENGTH,
                               f'Your First Name must be between {NAME_MIN_LENGTH} and {NAME_MAX_LENGTH} characters.')
        ]

    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=True,
        verbose_name='Last Name',
        validators=[
            NameValidator(),
            MinLengthValidator(NAME_MIN_LENGTH,
                               f'Your Last Name must be between {NAME_MIN_LENGTH} and {NAME_MAX_LENGTH} characters.'),
        ]
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date of Birth",
    )

    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Phone Number",
        help_text='Phone Number must be in format: 088888888.',
        validators=[
            MinLengthValidator(10, "Your Phone Number must be exactly 10 digits in given format!"),
            PhoneNumberValidator(),
        ]

    )

    address = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Address",
    )

    profile_picture = CloudinaryField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
