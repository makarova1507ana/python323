from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import LoginUserForm

class LoginUser(LoginView):
    form_class = LoginUserForm #LoginUserForm - немного модифицировали  / AuthenticationForm - это стандатрнтная форма
    template_name = 'users/sign_in.html'

    def get_success_url(self):
        return '../../' #reverse_lazy('home')

class LogoutUser(LogoutView):
    def get_success_url(self):
        return '../../' # костыльный выход на главную страницу