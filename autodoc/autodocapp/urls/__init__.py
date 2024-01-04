from django.urls import path, include

from ..views import logout_view, Authorization, index, PrintAboutSite

urlpatterns = [
    path('', index.as_view(), name='home'),  # Main menu
    path('authorization/', Authorization.as_view(), name='authorization'),
    path("logout/", logout_view, name="logout"),
    path('manager/', include('autodocapp.urls.manager')),
    path('storekeeper/', include('autodocapp.urls.storekeeper')),
    path('about/', PrintAboutSite.as_view(), name='about'),
]
