from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',  widget = forms.TextInput(attrs = {'class': 'form-input form-control'}))
    password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs = {'class': 'form-input form-control'}))


class CreateMarkForm(ModelForm):
    class Meta:
        model = Brands
        fields = ['brand']


class MarkForm(ModelForm):
    class Meta:
        model = Brands
        fields = ['brand']


class ModelForm(ModelForm):
    class Meta:
        model = Models
        fields = ['model']


class BrandsAndModelsForm(ModelForm):
    id_brand = forms.ModelChoiceField(queryset=Brands.objects)
    id_model = forms.ModelChoiceField(queryset=Models.objects)
    class Meta:
        model = BrandsAndModels
        fields = ['id_brand', 'id_model']


class CityForm(ModelForm):
    class Meta:
        model = Cities
        fields = ['city']

class StreetForm(ModelForm):
    class Meta:
        model = Streets
        fields = ['street']

