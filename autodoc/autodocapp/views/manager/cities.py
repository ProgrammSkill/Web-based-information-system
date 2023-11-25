from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView

from .. import CheckRole
from ...forms import CityForm
from ...models import Cities


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


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