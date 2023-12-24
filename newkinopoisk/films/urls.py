from django.urls import path, re_path
import films.views as film  #from films.views import index, movie, categories
urlpatterns = [

    path('', film.FilmsHome.as_view()),#extra_context={"title": "Custom Title"})),
    path('search_movie/', film.MovieList.as_view(), name='movie_search'),# http://127.0.0.1:8000/search_movie/page0

    path('suggestion/', film.SuggestGenre.as_view()),
    path('info_movie/<int:pk>/', film.MovieDetailView.as_view()),

    path('cats/', film.categories, name="media"), # http://127.0.0.1:8000/cats/


    re_path(r"^archive/(?P<year>(1|2)\d{3})/$", film.archive),


]