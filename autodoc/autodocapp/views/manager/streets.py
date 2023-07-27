from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from ..views import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

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