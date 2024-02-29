from django import forms
from django.contrib.auth.forms import AuthenticationForm
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

class ManufactureForm(ModelForm):
    class Meta:
        model = Manufacturers
        fields = ['manufacturer']


class StoreDepartmentsForm(ModelForm):
    class Meta:
        model = StoreDepartments
        fields = '__all__'


class SuppliersForm(ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'


class SupplyForm(ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'


class AutoPartsForm(ModelForm):
    class Meta:
        model = AutoParts
        fields = '__all__'
