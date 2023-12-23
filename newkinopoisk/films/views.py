import requests
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
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


def index(request):# http://127.0.0.1:8000/films/
    return render(request, f"films/index.html")

class FilmsHome(TemplateView):


    template_name = 'films/index.html'
    extra_context = {"title": "Custom Title",
                     'subscriptions': SubscriptionType.objects.all()  }

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def suggest_genre(request):
    if request.method == 'POST':
        form = SuggestGenreForm(request.POST, request.FILES)
        # print(request.POST)
        if form.is_valid(): # проверку в бэкэнд
            #print(form.cleaned_data) #очищенные данные
            try:
                # handle_uploaded_file(request.FILES["file"])# ошибка
                form.save() #Genres.objects.create(**form.cleaned_data)
                return redirect("/cats/")
            except:
                form.add_error(None, "Ошибка добавления данных")
    else:
        form = SuggestGenreForm()

    return render(request,
                  f"films/suggestion.html",
                  {'form': form})

class SuggestGenre(View):
    def get(self, request): # get -> method request
        form = SuggestGenreForm()
        return render(request,
                  f"films/suggestion.html",
                  {'form': form})
    def post(self, request): # post -> method request
        form = SuggestGenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() #Genres.objects.create(**form.cleaned_data)
            return redirect("/cats/")
        return render(request,
                      f"films/suggestion.html",
                      {'form': form})


def categories(request):# http://127.0.0.1:8000/films/cats/
    #genre = get_object_or_404(Genres, pk=1) # genre = row in Genres (slite3.db)
    genres = Genre.objects.all()

    data = {"genres": genres}

    return render(request, f"films/categories.html", data)

def get_info_movie(id_movie):
    req = requests.get(f"https://www.omdbapi.com/?apikey=23f82659&i={id_movie}")
    data = req.json() # очистить/изменить от пустых значений
    return data

def movie_pages(request, id_movie):# http://127.0.0.1:8000/films/info_movie/id={id_movie}
    data = get_info_movie(id_movie)  # делает запрос к апи на получение списка фильмо
    return render(request, f"films/info_movie.html", data)
def search_movies(request):
    movies_list  = Movie.objects.all()
    paginator = Paginator(movies_list, 10)  # Разбиваем на страницы по 10 элементов

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, показываем первую страницу
        movies = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы диапазона (например, 9999), показываем последнюю страницу
        movies = paginator.page(paginator.num_pages)

    data = {"movies": movies, "count": len(movies_list)}
    return render(request, "films/search_movie.html", data)

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




