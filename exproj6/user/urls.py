from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('signup/', views.create, name='create'),  # 사용자 등록
    path('signin/', views.form, name='form'),  # 로그인
    path('signout/', views.signout, name='signout'),  # 로그아웃
]
