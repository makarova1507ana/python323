import requests
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.base import TemplateView

from films.models import Genre, Movie, Subscription, SubscriptionType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SuggestGenreForm
from django.conf import settings  # Импорт настроек проекта


# genres = Genres.objects.all()
# print(genres) # в консоле перед запуском сервера отобразятся список моделей
paginator = None
#CBV - classes-based view -> показать страницу
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/


def pageNotFound(request, exception):
    return HttpResponseNotFound('<center><h1>Страница не найдена</h1></center>')



class FilmsHome(TemplateView):

    template_name = 'films/index.html'
    extra_context = {"title": "Custom Title",
                     'subscriptions_type': SubscriptionType.objects.all()  }

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)




class SuggestGenre(FormView):
    form_class = SuggestGenreForm
    template_name = 'films/suggestion.html'
    success_url = '/cats/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def categories(request):# http://127.0.0.1:8000/films/cats/
    #genre = get_object_or_404(Genres, pk=1) # genre = row in Genres (slite3.db)
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
    # метод, который будет формировать данные
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# **kwargs - пустой
        context["title"] = 'Matrix'
        #context["year"] = 1999
        return context

    # Ошибка не отдает данные
    #метод сортировки (по критерию)
    # def get_queryset(self):
    #     return Movie.objects.filter(title=self.kwargs['title']).select_related('title')



# def search_movies(request):
#     movies_list  = Movie.objects.all()
#     paginator = Paginator(movies_list, 10)  # Разбиваем на страницы по 10 элементов
#
#     page = request.GET.get('page')
#     try:
#         movies = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, показываем первую страницу
#         movies = paginator.page(1)
#     except EmptyPage:
#         # Если страница выходит за пределы диапазона (например, 9999), показываем последнюю страницу
#         movies = paginator.page(paginator.num_pages)
#
#     data = {"movies": movies, "count": len(movies_list)}
#     return render(request, "films/search_movie.html", data)

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




