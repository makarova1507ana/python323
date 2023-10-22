from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):# http://127.0.0.1:8000/films/
    return HttpResponse("Страница про фильмы")

def movie(request, id_movie):# http://127.0.0.1:8000/films/movie/{id_movie}
    data = {"header1": "страница про фильм",
            "id": id_movie
            }
     #данные из модели (БД)
    return render(request, "films/index.html", data)


def categories(request, cat_name):# http://127.0.0.1:8000/films/movie/{id_movie}
    return HttpResponse(f"Страница про {cat_name} категория ")

def archive(request, year):
    return HttpResponse(f"archive {year}")

    # if int(year) < 2023: return HttpResponse(f"archive {year}")
    # return Http404

