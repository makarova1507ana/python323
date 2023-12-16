from django.contrib import admin
from .models import *
import requests

from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import views

from django.urls import path

admin.site.register(SubscriptionOption)

#admin.site.register(Genre) # если  надо стандартное оформление
@admin.register(Genre)# если не надо стандартное оформление !!!!либо это!!!
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    ordering = ['title', 'time_create']

#admin.site.register(Genre, GenresAdmin) # если не надо стандартное оформление !!!!либо это!!!
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscribed_date', 'expiration_date', 'cost_type')

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    fields = ['type_name', 'cost_value', 'available_options', 'status']
    list_display = ('type_name', 'cost_value', 'display_options', 'status')
    list_editable = ('cost_value',)
    @admin.action(description="Сделать неактивными") # НЕ ОТОБРАЖАЕТСЯ В ДЖАНГО
    def set_disable(self, request, queryset):
        queryset.update(status=SubscriptionType.Status.DISABLE)
    filter_horizontal = ['available_options'] # переопределяет поведение листбокса со множественным выбором
    def display_options(self, obj): # на странице джанго отобразить список доступных опций
        return " | ".join([option.name for option in obj.available_options.all()])

    display_options.short_description = 'Доступные опции'

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'description', 'poster')

    # Переопределяем метод save_model для вызова create_movies_from_api при сохранении объекта Movie
    def save_model(self, request, obj, form, change):

        if not obj.description:  # Проверяем, заполнено ли поле 'description'
            obj.create_movies_from_api(obj.title)
        super().save_model(request, obj, form, change)


# надо переместить в save_model
    def response_change(self, request, obj):
        if "_addanother" in request.POST or "_continue" in request.POST:
            # Если нажата кнопка "Сохранить и добавить другой объект" или "Сохранить и продолжить редактирование"
            if not obj.description:  # Проверяем, заполнено ли поле 'description'
                obj.create_movie_from_api(obj.title)  # Вызываем метод create_movie_from_api, если поле description пустое
        return super().response_change(request, obj)


