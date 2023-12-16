# Generated by Django 4.2.6 on 2023-12-15 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_remove_movie_description_remove_movie_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.URLField(blank=True, default='/static/images/movie_base.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, default=1900, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 14, 21, 46, 54, 548609, tzinfo=datetime.timezone.utc)),
        ),
    ]
