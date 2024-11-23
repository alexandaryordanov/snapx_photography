from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.deconstruct import deconstructible


@deconstructible
class DateValidator:
    def __init__(self, msg=None):
        self.message = msg

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Date entered must be greater than today"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if value < timezone.now().date():
            raise ValidationError(self.message)
