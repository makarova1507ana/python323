# Generated by Django 4.2.6 on 2023-12-15 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_subscriptiontype_available_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 14, 19, 2, 7, 99927, tzinfo=datetime.timezone.utc)),
        ),
        migrations.RemoveField(
            model_name='subscriptiontype',
            name='available_options',
        ),
        migrations.AddField(
            model_name='subscriptiontype',
            name='available_options',
            field=models.ManyToManyField(to='films.subscriptionoption'),
        ),
    ]
