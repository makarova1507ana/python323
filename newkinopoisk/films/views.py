from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):# http://127.0.0.1:8000/films/
    return HttpResponse("Страница про фильмы")

def movie(request, id_movie):# http://127.0.0.1:8000/films/movie/{id_movie}
    return HttpResponse(f"Страница про {id_movie} фильм")


def categories(request, cat_name):# http://127.0.0.1:8000/films/movie/{id_movie}
    return HttpResponse(f"Страница про {cat_name} категория ")

