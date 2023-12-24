import requests
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.base import TemplateView

from films.models import Genre, Movie, Subscription, SubscriptionType
from django.core.paginator import Paginator
from .forms import SuggestGenreForm
from django.conf import settings  # Импорт настроек проекта



#CBV - classes-based view -> показать страницу
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/


def pageNotFound(request, exception):
    return HttpResponseNotFound('<center><h1>Страница не найдена</h1></center>')

class FilmsHome(TemplateView):

    template_name = 'films/index.html'
    extra_context = {"title": "Custom Title",
                     'subscriptions_type': SubscriptionType.objects.all()}

class SuggestGenre(FormView):
    form_class = SuggestGenreForm
    template_name = 'films/suggestion.html'
    success_url = '/cats/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def categories(request):# http://127.0.0.1:8000/films/cats/
    genres = Genre.objects.all()
    data = {"genres": genres}
    return render(request, f"films/categories.html", data)

class MovieDetailView(DetailView):
    template_name = "films/info_movie.html"
    model = Movie
    context_object_name = 'movie' # имя переменной для передачи конкретного фильма

class MovieList(ListView):
    template_name = "films/search_movie.html"
    model = Movie
    context_object_name = 'movies'
    paginate_by = 10 # сколько будет на одной странице

    # метод, который будет формировать данные
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = context['movies']
        context["title"] = self.request.GET.get('title', '')  # Передаем запрос в контекст для отображения в шаблоне
       # context["count"] = len(movies)


        return context

    #метод сортировки (по критерию)
    def get_queryset(self):
        query_title = self.request.GET.get('title')  # Получаем параметр запроса из URL
        query_year = self.request.GET.get('year')  # Получаем параметр запроса из URL
        if query_title:
            movies = Movie.objects.filter(title__icontains=query_title)  # Фильтруем фильмы по названию (независимо от регистра)
        else:
            movies = Movie.objects.all()# Если нет запроса, показываем все фильмы

        #фильтр по году
        if query_year:
            movies = movies.filter(year=query_year)
        return movies



def archive(request, year):
    return HttpResponse(f"archive {year}")

    # if int(year) < 2023: return HttpResponse(f"archive {year}")
    # return Http404


def transaction(request):
    if request.method == 'POST':
        # тестовые данные
        try:
            # получить данные о карте
            # обращение к методу апи -> придет ответ

            # ответ обработать(может придти ошибка транзкции (пример не хватает средств), или все успешно и т.д.)
            # и принять решение
                # и все хорошо (информация о транзакции успешная, и можно номер номер транзакции)
                # сохраняем данные в модель (ваше описание модели оплаты (чек номер(id)))
            pass
        except:
            pass
        pass
        #
    #return render(request, 'payment_form.html') #elseотображение странциы формой ввода карты




