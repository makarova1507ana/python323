# Generated by Django 4.2.6 on 2023-12-15 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_subscriptionoption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.URLField(default='/static/images/movie_base.jpg'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(default=1900, max_length=4),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 14, 19, 49, 11, 230116, tzinfo=datetime.timezone.utc)),
        ),
    ]
