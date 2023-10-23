from ..views import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def PrintSupply(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        supply = Supply.objects.all()
        autoParts = AutoParts.objects.all()
        suppliers = Suppliers.objects.all()

        context = {
            'role': role,
            'title': 'Поставки',
            'supply': supply,
            'autoParts': autoParts,
            'suppliers': suppliers
        }

        return render(request, 'autodocapp/supply.html', context)
    else:
        return redirect('authorization')


def SearchSupplyByAutoPart(request):
    if request.user.is_authenticated:
        role = CheckRole(request)
        autoParts = AutoParts.objects.all()
        suppliers = Suppliers.objects.all()

        try:
            supply = Supply.objects.filter(id_AutoParts=request.GET.get('q'))
        except:
            supply = Supply.objects.all()

        context = {
            'role': role,
            'title': 'Поставки',
            'supply': supply,
            'autoParts': autoParts,
            'suppliers': suppliers
        }

        return render(request, 'autodocapp/supply.html', context)
    else:
        return redirect('authorization')
