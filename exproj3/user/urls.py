from django.urls import path

from . import views


urlpatterns = [
    path('join/', views.user_create),  # 사용자 등록 URL 패턴.
    path('login/', views.user_login),  # 로그인 URL 패턴.
]
