from django.urls import path

from . import views


urlpatterns = [
    path('join/', views.user_create),
    path('login/', views.user_login),
]
