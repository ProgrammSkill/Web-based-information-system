from django.urls import path, include

from ..views import logout_view, Authorization, index

urlpatterns = [
    path('', index.as_view(), name='home'),  # Main menu
    path('authorization/', Authorization.as_view(), name='authorization'),
    path("logout/", logout_view, name="logout"),
    path('public/', include('autodocapp.urls.manager')),
]
