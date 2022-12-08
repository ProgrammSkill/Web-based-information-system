from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from . import models
import sqlite3
from django.contrib.auth import logout
from autodocapp.forms import LoginUserForm

conn = sqlite3.connect(r'D:\Веб-информационная система\autodoc\db.sqlite3', check_same_thread=False)

class index(TemplateView):
    # Checking on authorization in system
    def get(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            cursor = conn.cursor()
            id_autodocapp_customuser = cursor.execute("SELECT group_id FROM  autodocapp_customuser_groups WHERE customuser_id="+str(id)).fetchall()[0][0]
            role = cursor.execute("SELECT name FROM  auth_group WHERE id=" + str(id_autodocapp_customuser)).fetchall()[0][0]
            # if role == 'Администратор':
            #     menu = [{'name': 'Пользователи', 'url': 'test'}]
            #     return HttpResponse('Администратор')
            # elif role == 'Кладовщик':
            #     menu = [{'name': 'Справочник', 'url': 'test'}]
            #     return HttpResponse('Кладовщик')
            # elif role == 'Продавец':
            #     return HttpResponse('no')
            # elif role == 'Директор':
            #     return HttpResponse('no')
            return render(request, 'autodocapp/index.html', {'role': role, 'title': 'Главное меню'})

        else:
            return redirect('authorization')




class Authorization(LoginView):
    form_class = LoginUserForm
    template_name = 'autodocapp/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')


    # def get_success_url(self, request):
    #     return render(request, 'autodocapp/authorization.html')

    # form_class = AuthenticationForm
    # template_name = 'authorization.html'
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Авторизация")
    #     return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('home')
#
# def logout_user(request):
#     logout(request)
#     return redirect('login')


class Marks(TemplateView):
    def get(self, request):
        return render(request, 'autodocapp/marks.html')


def logout_view(request):
    logout(request)
    return redirect('authorization')