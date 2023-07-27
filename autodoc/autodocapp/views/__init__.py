from django.urls import path
from autodoc import settings
from django.contrib.auth.views import LogoutView

from .views import logout_view, Authorization, index

path('', index.as_view(), name='home'),  # Main menu
path('authorization/', Authorization.as_view(), name='authorization'),