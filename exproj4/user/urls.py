from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.create_user),  # 사용자 등록
    path('signin/', views.user_form),  # 로그인
]
