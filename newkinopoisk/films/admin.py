from django.contrib import admin
from .models import *
import requests
from django.contrib import messages

from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import views

from django.urls import path
from django.contrib import admin
from .models import Example

#-------------------------------------------АБСТРАКИЦИЯ КАК РАБОАТЕТ МОДЕЛИ В АДМИН ПАНЕЛИ---------------------------------------------------------#
class BaseAdmin(admin.ModelAdmin):
    # Основной функционал для административной панели

    def save_model(self, request, obj, form, change):
        # Логика сохранения модели
        super().save_model(request, obj, form, change)

    def response_change(self, request, obj):
        # Логика при изменении модели
        super().response_change(request, obj)

    def delete_model(self, request, obj):
        # Логика удаления модели
        obj.delete()

    def message_user_about_action(self, request, count, action_text):
        # Отправка сообщения пользователю об успешно выполненном действии
        self.message_user(request, f"{count} объектов было {action_text}.")

    actions = ['set_disable', 'set_available']  # Добавленные пользовательские действия

    # Методы действий, обновляющие статус объектов
    @admin.action(description="Сделать активными")
    def set_available(self, request, queryset):
        count = queryset.update(status=SubscriptionType.Status.AVAILABLE)
        self.message_user_about_action(request, count, "сделано доступными")

    @admin.action(description="Сделать неактивными")
    def set_disable(self, request, queryset):
        count = queryset.update(status=SubscriptionType.Status.DISABLE)
        self.message_user_about_action(request, count, "сделано недоступными")


    #----------------------------------- НЕ РАБОТАЕТ!
    # def image_preview(self, obj):
    #     # Метод для отображения превью изображения в административной панели
    #     if obj.image:
    #         return '<img src="%s" width="100" />' % obj.image.url
    #     return 'No Image'
    # image_preview.short_description = 'Image Preview'
    # image_preview.allow_tags = True

    # def file_link(self, obj):
    #     # Метод для создания ссылки на файл в административной панели
    #     if obj.file:
    #         return '<a href="%s">%s</a>' % (obj.file.url, obj.file.name)
    #     return 'No File'
    # file_link.short_description = 'File Link'
    # file_link.allow_tags = True

    list_per_page = 20  # Количество объектов на одной странице
@admin.register(Example)
class ExampleAdmin(BaseAdmin):
    # Определяем, какие поля будут отображаться в списке объектов
    list_display = ('id', 'name', 'description', 'created_at', 'is_active', 'count', 'price', 'image', 'file')
    # Определяем, какие поля будут являться ссылками на редактирование объекта в списке
    list_display_links = ('id', 'name')
    # Определяем, по каким полям можно осуществлять поиск
    search_fields = ('name', 'description', 'count')
    # Определяем фильтры сбоку списка объектов
    list_filter = ('is_active', 'created_at')
    # Добавляем возможность фильтрации по дате в верхней части списка объектов
    date_hierarchy = 'created_at'
    # Определяем порядок сортировки объектов
    ordering = ('-created_at', 'name')


    fieldsets = (
        # Группировка полей в разделы на странице редактирования объекта
        ('Обязательные параметры', {
            'fields': ('name', 'description')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at', 'updated_at', 'is_active', 'count', 'price', 'image', 'file'),
            'classes': ('collapse',),  # Добавляет класс collapse для скрытия раздела по умолчанию
        }),
    )

    readonly_fields = ('created_at', 'updated_at')  # Определяем поля только для чтения


admin.site.register(SubscriptionOption)

#-------------------------------------------КОНЕЦ---------------------------------------------------------#








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
    list_display = ('type_name', 'cost_value', 'status',  'display_options') #
    list_editable = ('cost_value', 'status')
    actions = ['set_disable', 'set_available', ]# добавление действий (помимо удалений)

    filter_horizontal = ['available_options'] # переопределяет поведение листбокса со множественным выбором
    def display_options(self, obj): # на странице джанго отобразить список доступных опций
        return " | ".join([option.name for option in obj.available_options.all()])

    display_options.short_description = 'Доступные опции'
    @admin.action(description="Сделать активными")
    def set_available(self, request, queryset):
        count = queryset.update(status=SubscriptionType.Status.AVAILABLE)
        self.message_user(request,f"{count} подписки теперь будут  доступны")
    @admin.action(description="Сделать неактивными")
    def set_disable(self, request, queryset):
        count = queryset.update(status=SubscriptionType.Status.DISABLE)
        self.message_user(request,f"{count} подписки теперь будут не доступны", messages.WARNING)

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


