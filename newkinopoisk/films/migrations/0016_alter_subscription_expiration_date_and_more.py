# Generated by Django 4.2.6 on 2023-12-16 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0015_alter_subscription_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 15, 18, 48, 6, 473967, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='status',
            field=models.BooleanField(choices=[(0, 'Не активна'), (1, 'активна')], default=1, verbose_name='Статус'),
        ),
    ]
