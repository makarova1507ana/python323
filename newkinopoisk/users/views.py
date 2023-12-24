from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from users.forms import LoginUserForm

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/sign_in.html'

    def get_success_url(self):
        return '../../'

