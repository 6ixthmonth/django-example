from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'user'
urlpatterns = [

    # template_name='registration/login.html'
    # next_page='accounts/profile/'
    # redirect_field_name='next'
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html', next_page='/'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', next_page='/'), name='login'),

    # next_page='registration/logged_out.html'
    # redirect_field_name='next'
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('join/', views.UserCreateView.as_view(), name='create'),

]
