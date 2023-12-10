from django.core.validators import FileExtensionValidator
from django.db import models

# когда создавать миграции и отправлять
# когда создается новая таблица или меняется архитектура старой

# в формате статьи



class Genres(models.Model): # Genres = таблица Genres в бд db.sqlite3
    # id == pk (primary key) джаго сам создаст
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, max_length=255,    validators=[
            FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif']),  # Валидация формата
           ])
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    # id_film = models.IntegerField()
    # зависимости от фильмов
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Жанры"
        verbose_name_plural = "Жанры"
    # добавить слаги и отображение
    # def get_abosulte_path(self):
    #     return reverse("http://127.0.0.1:8000/cats/")


# class Company(models.Model):
#     name = models.CharField(max_length=50)
# class Films(models.Model):# код, который из апи будет выставить информацию в таблицу
#     title = models.CharField(max_length=50)
#     company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
#     # models.PROTECT
#     # models.SET_DEFAULT
#     # models.DO_NOTHING
#     # models.CASCADE #Company при удаление, удалит и строки с films
