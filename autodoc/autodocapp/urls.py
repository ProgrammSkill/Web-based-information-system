from django.urls import path

from autodoc import settings
from .views import *
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index.as_view(), name='home'), #Main menu
    path('authorization/', Authorization.as_view(), name='authorization'),
    path('authorization/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('marks/', Marks, name='marks'),  # brands
    path('create_mark/', MarkCreateView.as_view(), name='create_mark'),  # create brand
    path('marks/delete_mark/<int:mark_id>/', delete_mark.as_view(), name='delete_mark'),
    path('edit_mark/<int:mark_id>', edit_mark.as_view(), name='edit_mark'),
    path('marks/search_mark/', SearchMark.as_view(), name='search_mark'),
    path('models/', PrintModels, name='models'),  # модели
    path('models/delete_model/<int:model_id>/', delete_model.as_view(), name='delete_model'),
    path('edit_model/<int:model_id>', edit_model.as_view(), name='edit_model'),
    path('create_model/', ModelCreateView.as_view(), name='create_model'),  # создание марки
    path('models/search_model/', SearchModel.as_view(), name='search_model'),
    path('brands_and_models/', Print_brand_and_models, name='brands_and_models'),  # list of links between brands and models
    path('create_brand_and_model/', BrandAndModelCreateView.as_view(), name='create_brand_and_model'),  # create
    path('edit_brand_and_model/<int:brand_and_model_id>/', BrandAndModelEditView.as_view(), name='edit_brand_and_model'),  # edit
    path('brands_and_models/delete_brand_and_model/<int:brand_and_model_id>/', delete_brand_and_model.as_view(), name='delete_brand_and_model'),
    path('cities/', PrintCities, name='cities'),
    path('models/search_model/', SearchCity.as_view(), name='search_city'),
    path('marks/delete_mark/<int:city_id>/', delete_city.as_view(), name='delete_city'),
    # path("logout/", LogoutView.as_view(), name="logout"),

]