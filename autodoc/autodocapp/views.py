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
