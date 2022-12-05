from django.contrib.auth import get_user_model
from django.db import models

from Blog.crispy_blog.models import Post

UserModel = get_user_model()


class Reservation(models.Model):
    CHOICES = (
        ('5:00 PM', '5:00 PM'),
        ('6:00 PM', '6:00 PM'),
        ('7:00 PM', '7:00 PM'),
        ('8:00 PM', '8:00 PM'),
        ('9:00 PM', '9:00 PM'),
    )

    full_name = models.CharField(max_length=30, )

    email = models.EmailField(max_length=254, )

    phone = models.CharField(max_length=20, )

    number_of_person = models.IntegerField()

    date = models.DateTimeField()

    time = models.CharField(
        max_length=10,
        choices=CHOICES,
    )

    special_request = models.TextField()

    def __str__(self):
        return f'Reservation from {self.full_name}'


class Message(models.Model):
    full_name = models.CharField(max_length=30, )

    phone = models.CharField(max_length=30, )

    email = models.EmailField(max_length=254, )

    message = models.TextField()

    def __str__(self):
        return f"Message from {self.full_name}"


class Menu(models.Model):
    CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )

    type_of_meal = models.CharField(
        max_length=30,
        choices=CHOICES,
    )

    name_of_the_food = models.CharField(
        max_length=30,
    )

    price = models.FloatField()

    photo = models.ImageField(
        upload_to='food_images'
    )

    description = models.TextField()

    def __str__(self):
        return f'{self.name_of_the_food} - {self.type_of_meal}'


class SpecialMenu(models.Model):
    CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )

    type_of_meal = models.CharField(
        max_length=30,
        choices=CHOICES,
    )

    name_of_the_food = models.CharField(
        max_length=30,
    )

    price = models.FloatField()

    photo = models.ImageField(
        upload_to='food_images'
    )

    description = models.TextField()

    best_offers = models.BooleanField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name_of_the_food} - {self.type_of_meal}'


class FoodLike(models.Model):
    food = models.ForeignKey(
        SpecialMenu,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class FoodComment(models.Model):

    comment_text = models.TextField()

    date_and_time_of_publication = models.DateTimeField(
        auto_now=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Comment from {self.user}'


class NewsLetter(models.Model):

    email = models.EmailField(
        max_length=50,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Send newsletter to {self.user}'