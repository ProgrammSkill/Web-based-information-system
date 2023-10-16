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
