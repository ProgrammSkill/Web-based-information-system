from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView

from ..views import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def Marks(request):
    # Checking on authorization in system
    if request.user.is_authenticated:
        role = CheckRole(request)
        marks = Brands.objects.all()
        return render(request, 'autodocapp/marks.html', {'role': role, 'title': 'Марки', 'marks': marks})
    else:
        return redirect('authorization')


class SearchMark(ListView):
    template_name = 'autodocapp/marks.html'
    context_object_name = 'Brands'

    def get(self, request):
        if request.user.is_authenticated:
            role = CheckRole(request)
            marks = Brands.objects.filter(brand__icontains=self.request.GET.get('q'))
            return render(request, 'autodocapp/marks.html', {'role': role, 'title': 'Марки', 'marks': marks})
        else:
            return redirect('authorization')


class delete_mark(View):
    def get(self, request, mark_id, *args, **kwargs):
        if is_ajax(request=request):
            mark = get_object_or_404(Brands, id=mark_id)
            # mark = Brands.objects.get()
            mark.delete()
            return JsonResponse({"message": "success"})
        return JsonResponse({"message": "Wrong request"})


class edit_mark(View):
    form_class = MarkForm

    def post(self, request, mark_id, *args, **kwargs):
        if is_ajax(request=request):
            mark = get_object_or_404(Brands, id=mark_id)
            data = {
                "brand": mark.brand
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                name_brand = form.cleaned_data['brand']

                if form.has_changed():
                    mark.brand = name_brand
                    mark.save()
                    return JsonResponse({'message': 'Success'})
                else:
                    return JsonResponse({'message': 'Данные не редактируются'})

            else:
                return JsonResponse({'message': 'Данные пустые'})

        else:
            return JsonResponse({'message': 'Неверный запрос'})


class MarkCreateView(View):
    form_class = MarkForm

    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('marks')