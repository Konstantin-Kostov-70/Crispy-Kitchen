# Generated by Django 4.1.2 on 2022-11-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('number_of_person', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.CharField(max_length=10)),
                ('special_request', models.TextField()),
            ],
        ),
    ]
