# Generated by Django 4.1.2 on 2022-11-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crispy_kitchen', '0006_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_type_of_meal', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=30)),
                ('sp_name_of_the_food', models.CharField(max_length=30)),
                ('sp_price', models.PositiveIntegerField()),
                ('sp_photo', models.ImageField(upload_to='food_images')),
                ('sp_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='photo',
            field=models.ImageField(upload_to='food_images'),
        ),
    ]
