from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Ensure this value contains only letters.'


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    IMAGE_UPLOAD_TO_DIR = 'profile/'

    IMAGE_MAX_SIZE_IN_MB = 5

    BUDGET_DEFAULT_AND_MIN_VALUE = 0

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )

    )
    last_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT_AND_MIN_VALUE,
        validators=(
            MinValueValidator(BUDGET_DEFAULT_AND_MIN_VALUE),
        )
    )
    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expenses(models.Model):
    TITLE_MAX_LEN = 15

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
    )
    image = models.URLField(
        null=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        null=False,
    )
