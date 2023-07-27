from django.urls import path

from autodoc import settings
from django.contrib.auth.views import LogoutView

from ..views.manager.brand_and_models import Print_brand_and_models, BrandAndModelCreateView, BrandAndModelEditView, \
    delete_brand_and_model
from ..views.manager.brands import Marks, MarkCreateView, delete_mark, edit_mark, SearchMark
from ..views.manager.cities import CityCreate, edit_city, delete_city, SearchCity, PrintCities
from ..views.manager.manufacturers import SearchManufacturer, PrintManufacturers, delete_manufacturer, \
    ManufacturerCreateView, edit_manufacturer
from ..views.manager.models import PrintModels, delete_model, edit_model, ModelCreateView, SearchModel
from ..views.manager.streets import SearchStreet, PrintStreets, delete_street, StreetCreateView, edit_street

urlpatterns = [
    path('marks/', Marks, name='marks'),
    path('create_mark/', MarkCreateView.as_view(), name='create_mark'),
    path('marks/delete_mark/<int:mark_id>/', delete_mark.as_view(), name='delete_mark'),
    path('edit_mark/<int:mark_id>', edit_mark.as_view(), name='edit_mark'),
    path('marks/search_mark/', SearchMark.as_view(), name='search_mark'),
    path('models/', PrintModels, name='models'),  # модели
    path('models/delete_model/<int:model_id>/', delete_model.as_view(), name='delete_model'),
    path('edit_model/<int:model_id>', edit_model.as_view(), name='edit_model'),
    path('create_model/', ModelCreateView.as_view(), name='create_model'),
    path('models/search_model/', SearchModel.as_view(), name='search_model'),
    path('brands_and_models/', Print_brand_and_models, name='brands_and_models'),
    path('create_brand_and_model/', BrandAndModelCreateView.as_view(), name='create_brand_and_model'),
    path('edit_brand_and_model/<int:brand_and_model_id>/', BrandAndModelEditView.as_view(), name='edit_brand_and_model'),
    path('brands_and_models/delete_brand_and_model/<int:brand_and_model_id>/', delete_brand_and_model.as_view(), name='delete_brand_and_model'),
    path('cities/create_city/', CityCreate.as_view(), name='create_city'),
    path('edit_city/<int:city_id>', edit_city.as_view(), name='edit_city'),
    path('cities/delete_city/<int:city_id>/', delete_city.as_view(), name='delete_city'),
    path('cities/search_city/', SearchCity.as_view(), name='search_city'),
    path('cities/', PrintCities, name='cities'),
    path('streets/search_street/', SearchStreet.as_view(), name='search_street'),
    path('streets/', PrintStreets, name='streets'),
    path('delete_street/<int:street_id>/', delete_street.as_view(), name='delete_street'),
    path('create_street/', StreetCreateView.as_view(), name='create_street'),
    path('edit_street/<int:street_id>', edit_street.as_view(), name='edit_street'),
    path('manufacturers/search_manufacturer/', SearchManufacturer.as_view(), name='search_manufacturer'),
    path('manufacturers/', PrintManufacturers, name='manufacturers'),
    path('manufacturers/delete_manufacturer/<int:manufacturer_id>/', delete_manufacturer.as_view(), name='delete_manufacturer'),
    path('create_manufacturer/', ManufacturerCreateView.as_view(), name='create_manufacturer'),
    path('edit_manufacturer/<int:manufacturer_id>', edit_manufacturer.as_view(), name='edit_manufacturer'),
]