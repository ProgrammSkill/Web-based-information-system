from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from ..views import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def PrintManufacturers(request):
    if request.user.is_authenticated:  # Checking on authorization in system
        role = CheckRole(request)
        mufacturers = Manufacturers.objects.all()
        return render(request, 'autodocapp/mufacturers.html', {'role': role, 'title': 'Производители', 'mufacturers': mufacturers})
    else:
        return redirect('authorization')

class SearchManufacturer(ListView):
    template_name = 'autodocapp/cities.html'
    context_object_name = 'Manufacturers'

    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            manufacturer = Manufacturers.objects.filter(manufacturer__icontains=self.request.GET.get('q'))
            return render(request, 'autodocapp/mufacturers.html', {'role': role, 'title': 'Производители', 'mufacturers': manufacturer})
        else:
            return redirect('authorization')

class delete_manufacturer(View):
    def get(self, request, manufacturer_id, *args, **kwargs):
        if is_ajax(request=request):
            manufacturer = get_object_or_404(Manufacturers, id=manufacturer_id)
            manufacturer.delete()
            return JsonResponse({"message": "Success"})
        return JsonResponse({"message": "Wrong request"})

class ManufacturerCreateView(View):
    form_class = ManufactureForm
    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('manufacturers')

class edit_manufacturer(View):
    form_class = ManufactureForm

    def post(self, request, manufacturer_id, *args, **kwargs):
        if is_ajax(request=request):
            manufacturer = get_object_or_404(Manufacturers, id=manufacturer_id)
            data = {
                "manufacturer": manufacturer.manufacturer
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                name_manufacturer = form.cleaned_data['manufacturer']

                if form.has_changed():
                    manufacturer.manufacturer = name_manufacturer
                    manufacturer.save()
                    return JsonResponse({'message': 'Success'})
                else:
                    return JsonResponse({'message': 'Данные не редактируются'})

            else:
                return JsonResponse({'message': 'Данные пустые'})

        else:
            return JsonResponse({'message': 'Неверный запрос'})
