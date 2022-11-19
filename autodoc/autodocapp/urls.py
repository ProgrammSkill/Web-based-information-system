from django.urls import path
from .views import *
from django.contrib import admin


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index.as_view(), name='home'), #Главное меню
    path('authorization/', Authorization.as_view(), name='authorization'), #Авторизация
]