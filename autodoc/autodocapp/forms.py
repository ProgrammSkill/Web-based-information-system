from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',  widget = forms.TextInput(attrs = {'class': 'form-input'}))
    password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs = {'class': 'form-input'}))


# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username',)