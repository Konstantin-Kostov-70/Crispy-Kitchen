# Generated by Django 4.1.2 on 2022-11-25 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crispy_blog', '0003_post_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='recipe',
        ),
    ]
