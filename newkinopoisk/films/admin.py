from django.contrib import admin
from .models import Genres

#admin.site.register(Genres) # если  надо стандартное оформление
@admin.register(Genres)# если не надо стандартное оформление !!!!либо это!!!
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    ordering = ['title', 'time_create']

#admin.site.register(Genres, GenresAdmin) # если не надо стандартное оформление !!!!либо это!!!