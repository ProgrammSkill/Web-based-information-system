# def CheckRole(request):
#     user = request.user
#     role = str(user.groups.all()[0])
#     return role
#
# class index(TemplateView):
#     # Checking on authorization in system
#     def get(self, request):
#         if request.user.is_authenticated:
#             role = CheckRole(request)
#             return render(request, 'autodocapp/index.html', {'role': role, 'title': 'Главное меню'})
#         else:
#             return redirect('authorization')
#
# class Authorization(LoginView):
#     form_class = LoginUserForm
#     template_name = 'autodocapp/authorization.html'
#     def get_success_url(self):
#         return reverse_lazy('home')
#
# def logout_view(request):
#     logout(request)
#     return redirect('authorization')
