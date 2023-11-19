from django.db import models

# в формате статьи
class Genres(models.Model): # Genres = таблица Genres в бд db.sqlite3
    title = models.CharField(max_length=50)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    # зависимости от фильмов
