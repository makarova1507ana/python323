from django.urls import path
import films.views as film  #from films.views import index, movie, categories

urlpatterns = [
    path('', film.index),  # http://127.0.0.1:8000/films/
    path('movie/<int:id_movie>/', film.movie), # http://127.0.0.1:8000/films/movie/{id}/
    path('categories/<slug:cat_name>/', film.categories), # http://127.0.0.1:8000/films/categories/{cat_name}/

]