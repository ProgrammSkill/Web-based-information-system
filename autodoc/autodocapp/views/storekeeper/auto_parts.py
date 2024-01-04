from django.shortcuts import redirect, render

from .. import CheckRole
from ...models import *


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
