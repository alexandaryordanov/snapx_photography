import magic
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ProfileImageValidator:
    def __init__(self, max_size=None, allowed_mime_types=None):
        self.max_size = max_size
        self.allowed_mime_types = allowed_mime_types or ['image/jpeg', 'image/png', 'image/gif']

    def __call__(self, value):
        if self.max_size and value.size > self.max_size:
            raise ValidationError(f"File size exceeds {self.max_size / (1024 * 1024):.2f} MB.")

        mime = magic.Magic(mime=True)
        file_mime = mime.from_buffer(value.read(2048))
        if file_mime not in self.allowed_mime_types:
            raise ValidationError(
                f"Unsupported file type. Allowed MIME types are: {', '.join(self.allowed_mime_types)}.")


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
