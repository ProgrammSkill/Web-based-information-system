from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView

from ..views import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

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