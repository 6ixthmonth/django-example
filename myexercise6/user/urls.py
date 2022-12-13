from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('join/', views.user_create, name='create'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
