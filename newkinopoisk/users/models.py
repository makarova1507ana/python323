from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

# Определение пользовательской модели User, которая наследуется от AbstractUser
class User(AbstractUser):
    # Добавление пользовательского поля date_birth для хранения даты рождения пользователя
    date_birth = models.DateField(null=False, default="1900-01-01")


