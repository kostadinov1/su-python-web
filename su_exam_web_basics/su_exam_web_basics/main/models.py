from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters, numbers and underscore.')


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    IMAGE_UPLOAD_TO_DIR = 'profile/'

    username = models.CharField(
        null=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    email = models.EmailField(
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    CHOICES = [('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'),
               ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'),
               ('County Music', 'County Music'), ('Dance Music', 'Dance Music'),
               ('Hip-Hop Music', 'Hip-Hop Music'), ('Other Music', 'Other Music')]

    name = models.CharField(
        null=False,
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )
    artist = models.CharField(
        null=False,
        max_length=ARTIST_MAX_LEN,
    )
    genre = models.CharField(
        null=False,
        max_length=GENRE_MAX_LEN,
        choices=CHOICES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()

    price = models.FloatField(
        null=False,
    )
    username_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('username_id', 'name')
