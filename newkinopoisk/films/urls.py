from django.urls import path, re_path
import films.views as film  #from films.views import index, movie, categories

urlpatterns = [
    path('', film.index),  # http://127.0.0.1:8000/films/
    path('<slug:name_page>/', film.movie_pages), # http://127.0.0.1:8000/films/{name_page}
    path('categories/<slug:cat_name>/', film.categories), # http://127.0.0.1:8000/films/categories/{cat_name}/

    # http://127.0.0.1:8000/films/test/
    path('test/', film.f), #для учебы

    # http://127.0.0.1:8000/films/archive/2000 - валидный
    re_path(r"^archive/(?P<year>(1|2)\d{3})/$", film.archive),
    #  1000 - 2999 - валидный
    # http://127.0.0.1:8000/films/archive/434324234 - невалидный

]