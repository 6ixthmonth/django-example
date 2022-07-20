from django.urls import path

from . import views


urlpatterns = [
    path('join/', views.user_create),  # 사용자 등록.
    path('login/', views.user_login),  # 로그인.
]
