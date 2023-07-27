from django.urls import path, include
from autodoc import settings
from django.contrib.auth.views import LogoutView
from ..views import Authorization, index


urlpatterns = [
    path('', index.as_view(), name='home'),  # Main menu
    path('authorization/', Authorization.as_view(), name='authorization'),
    path('authorization/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('public/', include('autodocapp.urls.manager')),
]