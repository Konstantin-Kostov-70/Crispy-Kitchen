# Generated by Django 4.1.2 on 2022-11-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crispy_kitchen', '0012_foodcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialmenu',
            name='best_offers',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
