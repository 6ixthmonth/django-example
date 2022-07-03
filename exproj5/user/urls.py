from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('signup/', views.create_user, name='signup'),  # 사용자 등록
    path('signin/', views.user_form, name='signin'),  # 로그인
]
