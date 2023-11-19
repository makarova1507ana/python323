from django.urls import path, re_path
import films.views as film  #from films.views import index, movie, categories

urlpatterns = [
    path('', film.index),  # http://127.0.0.1:8000/films/
    path('search_movie/page<int:page_number>/', film.search_movies),# http://127.0.0.1:8000/films/search_movie/page0

    path('info_movie/<slug:id_movie>/', film.movie_pages), # http://127.0.0.1:8000/films/info_movie/id_movie/
    path('categories/<slug:cat_name>/', film.categories), # http://127.0.0.1:8000/films/categories/{cat_name}/

    # http://127.0.0.1:8000/films/test/
    path('test/', film.f), #для учебы

    # http://127.0.0.1:8000/films/archive/2000 - валидный
    re_path(r"^archive/(?P<year>(1|2)\d{3})/$", film.archive),
    #  1000 - 2999 - валидный
    # http://127.0.0.1:8000/films/archive/434324234 - невалидный

]