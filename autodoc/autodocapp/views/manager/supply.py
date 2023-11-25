from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from models import *
from .. import CheckRole


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


class delete_supply(View):
    def get(self, request, supply_id, *args, **kwargs):
        if is_ajax(request=request):
            supply = get_object_or_404(Supply, id=supply_id)
            supply.delete()
            return JsonResponse({"message": "success"})
        return JsonResponse({"message": "Wrong request"})


class SupplyCreateView(View):
    # form_class = SupplyForm

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('supply')
    def post(self, request):
        id_supplier = request.POST.get('id_supplier')
        id_auto_parts = request.POST.get('id_AutoParts')
        purchase_price = request.POST.get('purchase_price')
        quantity = request.POST.get('quantity')
        delivery_date = request.POST.get('delivery_date')
        status = request.POST.get('status')
        print(delivery_date)

        supplier = Suppliers.objects.get(id=id_supplier)
        autoPart = AutoParts.objects.get(id=id_auto_parts)

        supply = Supply(id_supplier=supplier, id_AutoParts=autoPart, purchase_price=purchase_price, quantity=quantity,
                        delivery_date=delivery_date, status=status)
        supply.save()
        return redirect('supply')
