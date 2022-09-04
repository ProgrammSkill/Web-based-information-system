from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from autodocapp.forms import LoginUserForm


class index(TemplateView):
    # Checking on authorization in system
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'autodocapp/index.html')
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


# def Authorization(request):
#     return render(request, 'autodocapp/authorization.html')

#