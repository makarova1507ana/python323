from django.urls import path, re_path
import films.views as film  #from films.views import index, movie, categories
urlpatterns = [

    path('', film.FilmsHome.as_view()),#extra_context={"title": "Custom Title"})),
    path('search_movie/', film.search_movies),# http://127.0.0.1:8000/search_movie/page0

    path('suggestion/', film.SuggestGenre.as_view()),
    path('info_movie/<slug:id_movie>/', film.movie_pages), # http://127.0.0.1:8000/info_movie/id_movie/
    path('cats/', film.categories, name="media"), # http://127.0.0.1:8000/cats/


    re_path(r"^archive/(?P<year>(1|2)\d{3})/$", film.archive),


]