from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import requests
# когда создавать миграции и отправлять
# когда создается новая таблица или меняется архитектура старой

# в формате статьи



class Genre(models.Model): # Genres = таблица Genres в бд db.sqlite3
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




class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)  # Пример определения поля description
    poster = models.URLField( blank=True, null=True)  # Добавляем поле для хранения ссылки на постер
    #slug

    @classmethod #сохраняет сразу много фильмов (10 фильмов по апи)
    def create_movies_from_api(cls, search_query):
        omdb_api_key = '23f82659'  # Замените на ваш API-ключ от OMDB

        params = {
            'apikey': omdb_api_key,
            's': search_query,
        }

        response = requests.get('http://www.omdbapi.com/', params=params) #

        if response.status_code == 200:
            movie_data = response.json().get('Search', []) # словарь с фильмами
            #movies_to_create = []

            for movie_info in movie_data:
                movie_id = movie_info.get('imdbID')

                # Для каждого фильма делаем дополнительный запрос, чтобы получить подробную информацию
                params = {
                    'apikey': omdb_api_key,
                    'i': movie_id,
                }

                movie_response = requests.get('http://www.omdbapi.com/', params=params)

                if movie_response.status_code == 200:
                    detailed_movie_data = movie_response.json()
                    movie = cls(
                        title=detailed_movie_data.get('Title', ''),
                        year=detailed_movie_data.get('Year', ''),
                        director=detailed_movie_data.get('Director', ''),
                        description=detailed_movie_data.get('Plot', ''),
                        poster=detailed_movie_data.get('Poster', ''),
                    )
                    movie.save() #сохраняем конкретный фильм

            #cls.objects.bulk_create(movies_to_create)

    @classmethod #сохраняет 1 фильм (1 фильм по апи)
    def create_movie_from_api(cls, search_query):
        omdb_api_key = '23f82659'  # Замените на ваш API-ключ от OMDB

        params = {
            'apikey': omdb_api_key,
            't': search_query,  # Здесь используется search_query, переданный в методе
        }

        response = requests.get('http://www.omdbapi.com/', params=params)

        if response.status_code == 200:
            movie_data = response.json()
            if movie_data.get('Response') == 'True':
                # Создание нового объекта Movie с данными из API OMDB
                new_movie = cls(
                    title=movie_data.get('Title', ''),
                    year=movie_data.get('Year', ''),
                    director=movie_data.get('Director', ''),
                    description=movie_data.get('description', ''),
                    poster=movie_data.get('Poster', ''),
                )
                new_movie.save()


# Subscription будет хранить информацию об уже приобретенных подписках
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # джанго предоставляет User
    subscribed_date = models.DateField(auto_now_add=True)
    #duration_days = models.IntegerField(default=30) #доделать кол-во дней на подписку
    expiration_date = models.DateField(default=timezone.now() + timezone.timedelta(days=30))    #int(duration_days.value_to_string()))) # дата окончания подписки
    cost_type = models.ForeignKey('SubscriptionType', on_delete=models.SET_NULL, null=True)
    # информация о покупке

    def __str__(self):
        return f"{self.user.username}'s Subscription"

    class Meta:
        verbose_name = 'Приобретенная Подписка'
        verbose_name_plural = 'Приобретенные Подписки'


# доступные по поиске опции
class SubscriptionOption(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Доступная опция"
        verbose_name_plural = "Доступные опции"

# SubscriptionType информация о возможных подписках, которые можно выбрать
class SubscriptionType(models.Model):
    class Status(models.IntegerChoices):
        DISABLE = 0, 'Не активна'
        AVAILABLE = 1, 'активна'
    type_name = models.CharField(max_length=20, unique=True,  verbose_name="Название") # название
    cost_value = models.IntegerField(default=0, verbose_name="стоимость") #стоимость
    available_options = models.ManyToManyField(SubscriptionOption,  verbose_name="Доступные опции") # доступные по поиске опции
    status = models.BooleanField(choices=Status.choices, default=Status.AVAILABLE, verbose_name="Статус")
    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Тип Подписки"
        verbose_name_plural = "Типы Подписок"

# class Company(models.Model):
#     name = models.CharField(max_length=50)
# class Films(models.Model):# код, который из апи будет выставить информацию в таблицу
#     title = models.CharField(max_length=50)
#     company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
#     # models.PROTECT
#     # models.SET_DEFAULT
#     # models.DO_NOTHING
#     # models.CASCADE #Company при удаление, удалит и строки с films
