from django.urls import path

from ..views.storekeeper.auto_parts import PrintAutoParts, AutoPartsCreate

urlpatterns = [
    path('auto_parts/', PrintAutoParts, name='auto_parts'),
    path('create_auto_part/', AutoPartsCreate.as_view(), name='create_auto_part')
]
