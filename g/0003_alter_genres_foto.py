# Generated by Django 4.2.6 on 2023-11-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_genres_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='foto',
            field=models.BinaryField(verbose_name=b''),
        ),
    ]
