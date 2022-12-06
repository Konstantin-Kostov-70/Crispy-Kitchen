from django.db import models
from django.contrib.auth import models as auth_models


class UserProfile(auth_models.AbstractUser):
    pass
    username = models.CharField(
        max_length=20,
        unique=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )

    email = models.EmailField(
        max_length=50,
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    profession = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    photo = models.ImageField(
        upload_to='download_images',
        null=True,
        blank=True,

    )
