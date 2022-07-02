from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.create_user, name='create'),  # 사용자 등록
    path('signin/', views.user_form, name='form'),  # 로그인
]
