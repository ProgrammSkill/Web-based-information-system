from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView

from .. import CheckRole
from ...forms import BrandsAndModelsForm
from ...models import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


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


class SearchBrandsModelsByBrand(ListView):
    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            brands = Brands.objects.all()
            models = Models.objects.all()

            try:
                brand_and_models = BrandsAndModels.objects.filter(id_brand=self.request.GET.get('q'))
            except:
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