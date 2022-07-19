from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('join/', views.user_create, name='create'),  # 사용자 등록.
    path('login/', views.user_login, name='login'),  # 로그인.
    path('logout/', views.user_logout, name='logout'),  # 로그아웃.
]
