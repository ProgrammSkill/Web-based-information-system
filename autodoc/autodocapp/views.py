from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group, Permission, User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView
from . import models
from django.contrib.auth import logout
from autodocapp.forms import *
from .models import *
# from django.http import JsonResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def CheckRole(request):
    user = request.user
    role = str(user.groups.all()[0])
    return role

class index(TemplateView):
    # Checking on authorization in system
    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            return render(request, 'autodocapp/index.html', {'role': role, 'title': 'Главное меню'})

        else:
            return redirect('authorization')


class Authorization(LoginView):
    form_class = LoginUserForm
    template_name = 'autodocapp/authorization.html'
    def get_success_url(self):
        return reverse_lazy('home')


def Marks(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        marks = Brands.objects.all()
        return render(request, 'autodocapp/marks.html', {'role': role, 'title': 'Марки', 'marks': marks})
    else:
        return redirect('authorization')


class SearchMark(ListView):
    template_name = 'autodocapp/marks.html'
    context_object_name = 'Brands'

    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            marks = Brands.objects.filter(brand__icontains=self.request.GET.get('q'))
            return render(request, 'autodocapp/marks.html', {'role': role, 'title': 'Марки', 'marks': marks})
        else:
            return redirect('authorization')


class delete_mark(View):
    def get(self, request, mark_id, *args, **kwargs):
        if is_ajax(request=request):
            mark = get_object_or_404(Brands, id=mark_id)
            # mark = Brands.objects.get()
            mark.delete()
            return JsonResponse({"message": "success"})
        return JsonResponse({"message": "Wrong request"})


class edit_mark(View):
    form_class = MarkForm

    def post(self, request, mark_id, *args, **kwargs):
        if is_ajax(request=request):
            mark = get_object_or_404(Brands, id=mark_id)
            data = {
                "brand": mark.brand
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                name_brand = form.cleaned_data['brand']

                if form.has_changed():
                    mark.brand = name_brand
                    mark.save()
                    return JsonResponse({'message': 'Success'})
                else:
                    return JsonResponse({'message': 'Данные не редактируются'})

            else:
                return JsonResponse({'message': 'Данные пустые'})

        else:
            return JsonResponse({'message': 'Неверный запрос'})


class MarkCreateView(View):
    form_class = MarkForm

    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('marks')


def PrintModels(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        models = Models.objects.all()
        return render(request, 'autodocapp/models.html', {'role': role, 'title': 'Модели', 'models': models})
    else:
        return redirect('authorization')


class SearchModel(ListView):
    template_name = 'autodocapp/models.html'
    context_object_name = 'Models'

    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            models = Models.objects.filter(model__icontains=self.request.GET.get('q'))
            return render(request, 'autodocapp/models.html', {'role': role, 'title': 'Модели', 'models': models})
        else:
            return redirect('authorization')

class delete_model(View):
    def get(self, request, model_id, *args, **kwargs):
        if is_ajax(request=request):
            model = get_object_or_404(Models, id=model_id)
            # mark = Brands.objects.get()
            model.delete()
            return JsonResponse({"message": "Success"})
        return JsonResponse({"message": "Wrong request"})


class edit_model(View):
    form_class = ModelForm

    def post(self, request, model_id, *args, **kwargs):
        if is_ajax(request=request):
            model = get_object_or_404(Models, id=model_id)
            data = {
                "model": model.model
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                name_brand = form.cleaned_data['model']

                if form.has_changed():
                    model.model = name_brand
                    model.save()
                    return JsonResponse({'message': 'Success'})
                else:
                    return JsonResponse({'message': 'Данные не редактируются'})

            else:
                return JsonResponse({'message': 'Данные пустые'})

        else:
            return JsonResponse({'message': 'Неверный запрос'})


class ModelCreateView(View):
    form_class = ModelForm

    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('models')


def Print_brand_and_models(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        brands = Brands.objects.all()
        models = Models.objects.all()
        brand_and_models = BrandsAndModels.objects.all()

        context = {
            'role': role,
            'title': 'Связи между марками и моделями',
            'brands': brands,
            'models': models,
            'brand_and_models': brand_and_models
        }

        return render(request, 'autodocapp/brands_and_models.html', context)
    else:
        return redirect('authorization')


class delete_brand_and_model(View):
    def get(self, request, brand_and_model_id, *args, **kwargs):
        if is_ajax(request=request):
            BrandAndModel = get_object_or_404(BrandsAndModels, id=brand_and_model_id)
            BrandAndModel.delete()
            return JsonResponse({"message": "Success"})
        return JsonResponse({"message": "Wrong request"})


class BrandAndModelCreateView(View):
    form_class = BrandsAndModelsForm

    def post(self, request,  *args, **kwargs):
        form = BrandsAndModelsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('brands_and_models')


class BrandAndModelEditView(View):
    form_class = BrandsAndModelsForm

    def post(self, request, brand_and_model_id, *args, **kwargs):
        if is_ajax(request=request):
            brand_and_model = get_object_or_404(BrandsAndModels, id=brand_and_model_id)
            data = {
                "id_brand": brand_and_model.id_brand,
                "id_model": brand_and_model.id_model
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                id_brand = form.cleaned_data['id_brand']
                id_model = form.cleaned_data['id_model']

                if form.has_changed():
                    brand_and_model.id_brand = id_brand
                    brand_and_model.id_model = id_model
                    brand_and_model.save()
                    return JsonResponse({'message1': 'Success'})
                else:
                    return JsonResponse({'message2': 'Данные не редактируются'})

            else:
                return JsonResponse({'message3': 'Данные пустые'})

        else:
            return JsonResponse({'message4': 'Неверный запрос'})


def PrintCities(request):
    if request.user.is_authenticated:  # Checking on authorization in system
        role = CheckRole(request)
        cities = Cities.objects.all()
        return render(request, 'autodocapp/cities.html', {'role': role, 'title': 'Города', 'cities': cities})
    else:
        return redirect('authorization')


class SearchCity(ListView):
    template_name = 'autodocapp/cities.html'
    context_object_name = 'Cities'

    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            cities = Cities.objects.filter(city__icontains=self.request.GET.get('q'))
            return render(request, 'autodocapp/cities.html', {'role': role, 'title': 'Города', 'cities': cities})
        else:
            return redirect('authorization')


class delete_city(View):
    def get(self, request, city_id, *args, **kwargs):
        if is_ajax(request=request):
            city = get_object_or_404(Cities, id=city_id)
            city.delete()
            return JsonResponse({"message": "success"})
        return JsonResponse({"message": "Wrong request"})


class CityCreate(View):
    form_class = CityForm
    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cities')


class edit_city(View):
    form_class = CityForm

    def post(self, request, city_id, *args, **kwargs):
        if is_ajax(request=request):
            city = get_object_or_404(Cities, id=city_id)
            data = {
                "city": city.city
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                name_city = form.cleaned_data['city']

                if form.has_changed():
                    city.brand = name_city
                    city.save()
                    return JsonResponse({'message': 'Success'})
                else:
                    return JsonResponse({'message': 'Данные не редактируются'})

            else:
                return JsonResponse({'message': 'Данные пустые'})

        else:
            return JsonResponse({'message': 'Неверный запрос'})


def PrintStreets(request):
    if request.user.is_authenticated:  # Checking on authorization in system
        role = CheckRole(request)
        streets = Streets.objects.all()
        return render(request, 'autodocapp/streets.html', {'role': role, 'title': 'Улицы', 'streets': streets})
    else:
        return redirect('authorization')

class SearchStreet(ListView):
    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            print(self.request.GET.get('q'))
            streets = Streets.objects.filter(street__icontains=self.request.GET.get('q'))
            return render(request, 'autodocapp/streets.html', {'role': role, 'title': 'Улицы', 'streets': streets})
        else:
            return redirect('authorization')

class delete_street(View):
    def get(self, request, street_id, *args, **kwargs):
        if is_ajax(request=request):
            street = get_object_or_404(Streets, id=street_id)
            street.delete()
            return JsonResponse({"message": "success"})
        return JsonResponse({"message": "Wrong request"})

class StreetCreateView(View):
    form_class = StreetForm
    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('streets')

class edit_street(View):
    form_class = StreetForm

    def post(self, request, street_id, *args, **kwargs):
        if is_ajax(request=request):
            street = get_object_or_404(Streets, id=street_id)
            data = {
                "street": street.street
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                name_street = form.cleaned_data['street']

                if form.has_changed():
                    street.street = name_street
                    street.save()
                    return JsonResponse({'message': 'Success'})
                else:
                    return JsonResponse({'message': 'Данные не редактируются'})

            else:
                return JsonResponse({'message': 'Данные пустые'})

        else:
            return JsonResponse({'message': 'Неверный запрос'})


def logout_view(request):
    logout(request)
    return redirect('authorization')
