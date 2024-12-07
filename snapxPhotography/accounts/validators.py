from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, msg=None):
        self.message = msg

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PhoneNumberValidator:
    def __init__(self, msg=None):
        self.message = msg

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your Phone Number must be exactly 10 digits in given format!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not value.isdigit() or value[0] != '0':
            raise ValidationError(self.message)
