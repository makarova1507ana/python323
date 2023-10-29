from django.http import HttpResponse, Http404
from django.shortcuts import render
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


# Create your views here.
def index(request):# http://127.0.0.1:8000/films/
    return HttpResponse("Страница про фильмы")

def movie_pages(request, name_page):# http://127.0.0.1:8000/films/{name_page}
    data = {
        'menu': ['menu1', 'menu2'],
    }
    if name_page in ['info_movie', "search_movie"]:
        return render(request, f"films/{name_page}.html", data)
    return Http404#("<h1>page not found</h1>")


def categories(request, cat_name):# http://127.0.0.1:8000/films/movie/{id_movie}
    return HttpResponse(f"Страница про {cat_name} категория ")

def archive(request, year):
    return HttpResponse(f"archive {year}")

    # if int(year) < 2023: return HttpResponse(f"archive {year}")
    # return Http404

