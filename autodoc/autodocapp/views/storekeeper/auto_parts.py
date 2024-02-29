from django.shortcuts import redirect, render
from django.views import View

from .. import CheckRole
from ...forms import AutoPartsForm
from ...models import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def PrintAutoParts(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        brands_and_models = BrandsAndModels.objects.all()
        brands = Brands.objects.all()
        models = Models.objects.all()
        manufacturers = Manufacturers.objects.all()
        auto_parts = AutoParts.objects.all()

        context = {
            'role': role,
            'title': 'Список автозапчастей',
            'brands_and_models': brands_and_models,
            'brands': brands,
            'models': models,
            'manufacturers': manufacturers,
            'auto_parts': auto_parts
        }

        return render(request, 'autodocapp/auto_parts.html', context)
    else:
        return redirect('authorization')


class AutoPartsCreate(View):
    form_class = AutoPartsForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('dcsdsd')
            form.save()
        return redirect('auto_parts')
