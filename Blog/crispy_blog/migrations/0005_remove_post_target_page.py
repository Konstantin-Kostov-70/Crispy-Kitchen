# Generated by Django 4.1.2 on 2022-11-25 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crispy_blog', '0004_remove_post_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='target_page',
        ),
    ]
