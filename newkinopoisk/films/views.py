import requests
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):# http://127.0.0.1:8000/films/
    return HttpResponse("Страница про фильмы")

def movie_pages(request, id_movie):# http://127.0.0.1:8000/films/info_movie/id={id_movie}
    return render(request, f"films/info_movie.html")



def categories(request, cat_name):# http://127.0.0.1:8000/films/movie/{id_movie}
    return HttpResponse(f"Страница про {cat_name} категория ")

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



def get_pages(page_number):
    if page_number == 1:
        return (1, 2, 3) # (10, еще 10, еще 10)
    elif page_number > 1:
        return (page_number + 2, page_number + 3, page_number + 4)
    else:
        return (1,)


def get_movies(request, page_number):
    #if request.POST.get("search_field") != None: #request.POST.get("search_field") обратились к телу запроса POST и к атрибут "search_field"
    name = request.POST.get("search_field", "Matrix")
    pages = get_pages(page_number) #pages = (1, 2, 3) - номера страниц для апи
    result = {'totalResults': 0, 'Search': []}
    count_pages = 0
    for i in range(len(pages)):
        try:
            req = requests.get(f"https://www.omdbapi.com/?apikey=23f82659&s={name}&page={pages[i]}")
            result['Response'] = req.json()['Response']
            # 1 проверить  есть ли найденные фильм
            if result['Response'] == 'False':      #!посмотри на Search перед return!
                return {'Error': result['Error']}
            result['Search'] += req.json()['Search']
            result['totalResults'] = req.json()['totalResults']
            count_pages = int(result['totalResults']) // 30

        except:
            break


    return {'response': result,
            'count_pages': list(range(1, count_pages+1))}
def search_movies(request, page_number):
    data = get_movies(request, page_number) # делает запрос к апи на получение списка фильмов
    return render(request, f"films/search_movie.html", data)

