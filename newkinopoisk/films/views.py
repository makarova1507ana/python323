import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.base import TemplateView

from films.models import Genre, Movie, Subscription, SubscriptionType
from django.core.paginator import Paginator
from .forms import SuggestGenreForm
from django.conf import settings  # Импорт настроек проекта



#CBV - classes-based view -> показать страницу
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/


def pageNotFound(request, exception):
    return HttpResponseNotFound('<center><h1>Страница не найдена</h1></center>')

class FilmsHome(TemplateView):

    template_name = 'films/index.html'
    extra_context = {"title": "Custom Title",
                     'subscriptions_type': SubscriptionType.objects.all()}

class SuggestGenre(FormView):
    form_class = SuggestGenreForm
    template_name = 'films/suggestion.html'
    success_url = '/cats/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def categories(request):# http://127.0.0.1:8000/films/cats/
    genres = Genre.objects.all()
    data = {"genres": genres}
    return render(request, f"films/categories.html", data)

class MovieDetailView(DetailView):
    template_name = "films/info_movie.html"
    model = Movie
    context_object_name = 'movie' # имя переменной для передачи конкретного фильма

class MovieList(ListView):
    template_name = "films/search_movie.html"
    model = Movie
    context_object_name = 'movies'
    paginate_by = 10 # сколько будет на одной странице

    # метод, который будет формировать данные
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = context['movies']
        context["title"] = self.request.GET.get('title', '')  # Передаем запрос в контекст для отображения в шаблоне
       # context["count"] = len(movies)


        return context

    #метод сортировки (по критерию)
    def get_queryset(self):
        query_title = self.request.GET.get('title')  # Получаем параметр запроса из URL
        query_year = self.request.GET.get('year')  # Получаем параметр запроса из URL
        if query_title:
            movies = Movie.objects.filter(title__icontains=query_title)  # Фильтруем фильмы по названию (независимо от регистра)
        else:
            movies = Movie.objects.all()# Если нет запроса, показываем все фильмы

        #фильтр по году
        if query_year:
            movies = movies.filter(year=query_year)
        return movies

class BuySubscription(TemplateView, LoginRequiredMixin):
    template_name = 'films/buy_subscription.html'
    extra_context = {'subscriptions_type': SubscriptionType.objects.all()}

def archive(request, year):
    return HttpResponse(f"archive {year}")

    # if int(year) < 2023: return HttpResponse(f"archive {year}")
    # return Http404


# ------------------------------------- обработка платежа ---------------------------------------#
# views.py
from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse

import stripe # надо устанавливать
# Устанавливаем секретный ключ Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentView(View):
    template_name = 'films/payment_form.html'

    def get(self, request, *args, **kwargs):
        # Обработка GET-запроса, отображение формы оплаты
        print("оплата ...")
        return render(request, self.template_name, {'publishable_key': settings.STRIPE_PUBLIC_KEY})

    def post(self, request, *args, **kwargs):
        # Получите данные о транзакции из формы
        token = request.POST.get('stripeToken')
        amount = 1000  # сумма в центах (например, $10.00)

        try:
            # Создайте платежную транзакцию через Stripe API
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Оплата заказа в вашем магазине',
            )
            print("оплата прошла")
            # Здесь может быть логика обработки успешного платежа
            return redirect('payment_success')  # Перенаправление на страницу успешной оплаты
        # return JsonResponse({'message': 'Платеж успешно проведен!'})

        except stripe.error.CardError as e:
            # Ошибка с картой
            print("Ошибка с картой")
            return JsonResponse({'error': str(e)})

        except stripe.error.StripeError as e:
            # Остальные ошибки Stripe
            print("Остальные ошибки")
            return JsonResponse({'error': str(e)})


# views.py
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class PaymentSuccessView(View):
    template_name = 'films/payment_success.html'

    def get(self, request, *args, **kwargs):
        # Отображение страницы успешной оплаты
        return render(request, self.template_name)
