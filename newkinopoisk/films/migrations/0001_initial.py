# Generated by Django 4.2.6 on 2024-01-17 21:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Введите описание', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата последнего обновления записи')),
                ('is_active', models.BooleanField(default=True, help_text='Активный статус')),
                ('count', models.IntegerField(help_text='Количество чего-то')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена товара', max_digits=10)),
                ('image', models.ImageField(help_text='Изображение товара', upload_to='images/')),
                ('file', models.FileField(help_text='Файл', upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(max_length=255, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])])),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Жанры',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
                ('poster', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Доступная опция',
                'verbose_name_plural': 'Доступные опции',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('cost_value', models.IntegerField(default=0, verbose_name='стоимость')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Не активна'), (1, 'активна')], default=1, verbose_name='Статус')),
                ('available_options', models.ManyToManyField(to='films.subscriptionoption', verbose_name='Доступные опции')),
            ],
            options={
                'verbose_name': 'Тип Подписки',
                'verbose_name_plural': 'Типы Подписок',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_date', models.DateField(auto_now_add=True)),
                ('duration_days', models.IntegerField(default=30)),
                ('cost_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.subscriptiontype')),
            ],
            options={
                'verbose_name': 'Приобретенная Подписка',
                'verbose_name_plural': 'Приобретенные Подписки',
            },
        ),
    ]
