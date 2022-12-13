from django.db import models
from django.contrib.auth import models as auth_models
from cloudinary.models import CloudinaryField


class UserProfile(auth_models.AbstractUser):
    pass
    username = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    date_of_birth = models.DateField(
        null=True,
    )

    email = models.EmailField(
        max_length=50,
        unique=True
    )

    phone = models.CharField(
        max_length=20,

    )

    profession = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    photo = CloudinaryField('image')