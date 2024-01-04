from django.urls import path

from ..views.storekeeper.auto_parts import PrintAutoParts

urlpatterns = [
    path('auto_parts/', PrintAutoParts, name='auto_parts'),
]
