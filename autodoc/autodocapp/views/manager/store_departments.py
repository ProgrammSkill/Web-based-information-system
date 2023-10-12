from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from ..views import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def PrintStoreDepartments(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        cities = Cities.objects.all()
        streets = Streets.objects.all()
        shops = StoreDepartments.objects.all()

        context = {
            'role': role,
            'title': 'Список магазинов',
            'cities': cities,
            'streets': streets,
            'shops': shops
        }


        return render(request, 'autodocapp/store_departments.html', context)
    else:
        return redirect('authorization')


class StoreDepartmentEditView(View):
    form_class = StoreDepartmentsForm

    def post(self, request, store_department_id, *args, **kwargs):
        if is_ajax(request=request):
            store_department = get_object_or_404(StoreDepartments, id=store_department_id)
            data = {
                "id_city": store_department.id_city,
                "id_street": store_department.id_street,
                "house": store_department.house,
                "telephone": store_department.telephone
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                id_city = form.cleaned_data['id_city']
                id_street = form.cleaned_data['id_street']
                house = form.cleaned_data['house']
                telephone = form.cleaned_data['telephone']

                if form.has_changed():
                    store_department.id_city = id_city
                    store_department.id_street = id_street
                    store_department.house = house
                    store_department.telephone = telephone
                    store_department.save()

                    return JsonResponse({'message1': 'Success'})
                else:
                    return JsonResponse({'message2': 'Данные не редактируются'})

            else:
                return JsonResponse({'message3': 'Данные пустые'})

        else:
            return JsonResponse({'message4': 'Неверный запрос'})


class StoreDepartmentsCreateView(View):
    form_class = StoreDepartmentsForm
    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('store_departments')


class DeleteStoreDepartment(View):
    def get(self, request, store_departments_id, *args, **kwargs):
        if is_ajax(request=request):
            shop = get_object_or_404(StoreDepartments, id=store_departments_id)
            shop.delete()
            return JsonResponse({"message": "Success"})
        return JsonResponse({"message": "Wrong request"})
