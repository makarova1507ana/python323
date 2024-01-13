# Generated by Django 4.2.6 on 2023-12-15 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_subscriptiontype_alter_subscription_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 14, 18, 44, 27, 296508, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='type_name',
            field=models.CharField(choices=[('basic', 'Basic'), ('standard', 'Standard'), ('premium', 'Premium')], max_length=20, unique=True),
        ),
    ]