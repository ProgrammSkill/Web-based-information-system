from django.urls import path
from .views import *
from django.contrib import admin


urlpatterns = {
    path('admin/', admin.site.urls),
    path('', index), #Главное меню
    path('authorization/', Authorization), #Авторизация
}