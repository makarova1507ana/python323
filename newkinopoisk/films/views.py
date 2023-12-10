import requests
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from films.models import Genres
from django.core.paginator import Paginator
from .forms import SuggestGenreForm
from django.conf import settings  # Импорт настроек проекта

# genres = Genres.objects.all()
# print(genres) # в консоле перед запуском сервера отобразятся список моделей
paginator = None






# Create your views here.
def index(request):# http://127.0.0.1:8000/films/
    return render(request, f"films/index.html")

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# пример распаковки значений
# def foo(x, y):
#     print(x, y)
#
# d = {'x': 1, 'y': 2}
# foo(**d)
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

def pageNotFound(request, exception):
    return HttpResponseNotFound('<center><h1>Страница не найдена</h1></center>')
def get_info_movie(id_movie):
    req = requests.get(f"https://www.omdbapi.com/?apikey=23f82659&i={id_movie}")
    data = req.json() # очистить/изменить от пустых значений
    return data

def movie_pages(request, id_movie):# http://127.0.0.1:8000/films/info_movie/id={id_movie}
    data = get_info_movie(id_movie)  # делает запрос к апи на получение списка фильмо
    return render(request, f"films/info_movie.html", data)



def categories(request):# http://127.0.0.1:8000/films/cats/
    #genre = get_object_or_404(Genres, pk=1) # genre = row in Genres (slite3.db)
    genres = Genres.objects.all()

    data = {"genres": genres}

    return render(request, f"films/categories.html", data)

def archive(request, year):
    return HttpResponse(f"archive {year}")

    # if int(year) < 2023: return HttpResponse(f"archive {year}")
    # return Http404
def g(word):
    return word*2

class A:
    def __init__(self, a, b):
        self.a = a
        self.__b = b

    def get_b(self):
        return self.__b


# http://127.0.0.1:8000/films/test/
def f(request):
    #блок обработки данных
    data = {
        'movies': [{'id': 1, 'title': 'Movie1', 'description': 'description1'}, {'id': 2, 'title': 'Movie2', 'description': 'description2'}, {'id': 3, 'title': 'Movie3', 'description': 'description3'}],
        'title': 'учебная страница',
        'menu': ['About', 'page1', g("page2")],
        'num_float': 2.5,
        'num_int': 5,
        'set': {1, 5, 5, 5, 6},
        'dict': {'1': 1, 2: 2},
        'obj': A(5, 6),
    }

    return render(request, "edu/example.html", data)








def get_pages(page_number, title):
    page_number = int(page_number)
    req = requests.get(f"https://www.omdbapi.com/?apikey=23f82659&s={title}")
    totalResults = int(req.json()['totalResults'])
    if page_number == 1:
        return (1, 2, 3) # (10, еще 10, еще 10)
    elif page_number > 1:
        if totalResults//30 < page_number+2:
            return (page_number-1, page_number, page_number + 1)
        if totalResults//30 < page_number + 3 :
            return (page_number, page_number+1 ,page_number + 2)
        if  totalResults//30  <page_number +4:
            return (page_number+1, page_number+2 ,page_number + 3)
        return (page_number + 2, page_number + 3, page_number + 4)
    else:
        return (1,)


def get_movies(request):
    #if request.POST.get("search_field") != None: #request.POST.get("search_field") обратились к телу запроса POST и к атрибут "search_field"
    if request.POST:

        title = request.POST.get("search_film")
        if title == None:
            return {'Error': "No film"}
    else:

        title = request.GET.get("title")

    pages = get_pages(request.GET.get("page",1), title) #pages = (1, 2, 3) - номера страниц для апи
    result = {'totalResults': 0, 'Search': [], 'title': title}
    count_pages = 0
    for i in range(len(pages)):
        try:
            req = requests.get(f"https://www.omdbapi.com/?apikey=23f82659&s={title}&page={pages[i]}")
            result['Response'] = req.json()['Response']
            # 1 проверить  есть ли найденные фильм
            if result['Response'] == 'False':      #!посмотри на Search перед return!
                return {'Error': result['Error']}
            result['Search'] += req.json()['Search']
            result['totalResults'] = req.json()['totalResults']


        except:
            break


    return {'response': result,
            'count_pages': pages}


def search_movies(request):
    data = get_movies(request) # делает запрос к апи на получение списка фильмов

    return render(request, f"films/search_movie.html", data)

