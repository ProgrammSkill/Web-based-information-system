from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from ..views import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def PrintSuppliers(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        suppliers = Suppliers.objects.all()
        return render(request, 'autodocapp/suppliers.html',
                      {'role': role, 'title': 'Поставщики', 'suppliers': suppliers})
    else:
        return redirect('authorization')


def SearchSupplier(request):
    if request.user.is_authenticated:
        role = CheckRole(request)
        suppliers = Suppliers.objects.filter(title__icontains=request.GET.get('q'))
        return render(request, 'autodocapp/suppliers.html',
                      {'role': role, 'title': 'Поставщики', 'suppliers': suppliers})
    else:
        return redirect('authorization')


class SupplierCreateView(View):
    form_class = SuppliersForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('suppliers')


class delete_supplier(View):
    def get(self, request, supplier_id, *args, **kwargs):
        if is_ajax(request=request):
            supplier = get_object_or_404(Suppliers, id=supplier_id)
            supplier.delete()
            return JsonResponse({"message": "success"})
        return JsonResponse({"message": "Wrong request"})
