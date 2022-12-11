from django.contrib.auth import get_user_model
from django.db import models
from cloudinary.models import CloudinaryField

UserModel = get_user_model()


class Post(models.Model):
    CHOICES = (
        ('big photo', 'big photo'),
        ('small photo', 'small photo'),
    )

    photo_size = models.CharField(
        max_length=15,
        choices=CHOICES,

    )

    title = models.CharField(
        max_length=50,
    )

    date_of_publication = models.DateField(
        auto_now_add=True,
    )

    topic = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return f'{self.title}'

    photo = CloudinaryField('image')

    you_tube_code = models.CharField(
        max_length=20
    )








