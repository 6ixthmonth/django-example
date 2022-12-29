from django.contrib import admin
from django.urls import path, include, reverse_lazy

from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('board:list'))),
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
]
