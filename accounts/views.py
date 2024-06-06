from django.shortcuts import render
from django.views import generic #genericの中のビューを全部持ってきてくれる。
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm, CustomUserCreationForm,LoginAuthenticationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView


class AccountCreateView(generic.CreateView):
    Model = User
    form_class = UserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/accounts_create"


class AccountCreateViewUsingMyForm(generic.CreateView):
    Model = User
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/accounts_create_with_form"


class CustomAccountCreationView(generic.CreateView):
    Model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = '/accounts/custom_accounts_create'


class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginAuthenticationForm


class Logout(LogoutView):
    next_page = '/accounts/login'


class Home(TemplateView):
    template_name = 'accounts/home.html'