from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'user'
urlpatterns = [

    # 로그인 뷰를 연결하는 URL 패턴. 내장 뷰를 사용하여 로그인 페이지로 이동하거나 로그인을 처리한다. 다음과 같은 인수를 전달할 수 있다.
    # template_name: 로그인 하고자 할 때(GET 요청 시) 표시할 템플릿 이름. 즉, 로그인 페이지에 해당하는 HTML 파일의 경로와 이름. 기본 값은 'registration/login.html'.
    # next_page: 로그인 처리 후(POST 요청 시) 리다이렉트할 URL. 기본 값은 '/accounts/profile/'.
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', next_page='/'), name='login'),

    # 로그아웃 뷰를 연결하는 URL 패턴. 내장 뷰를 사용하여 로그아웃을 처리한다. 다음과 같은 인수를 전달할 수 있다.
    # template_name: 로그아웃 처리 후 표시할 템플릿 이름. 리다이렉트 하지 않음. 기본 값은 'registration/logged_out.html'.
    # next_page: 로그아웃 처리 후 리다이렉트할 URL. 기본 값은 None.
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # 사용자 등록 뷰를 연결하는 URL 패턴. 사용자 정의 뷰를 사용하여 사용자 등록 페이지로 이동하거나 신규 사용자 데이터를 저장한다.
    path('join/', views.UserCreateView.as_view(), name='create'),

    # 사용자 정보 수정 뷰를 연결하는 URL 패턴.
    path('edit/<int:pk>', views.UserUpdateView.as_view(), name='update'),

    # 사용자 탈퇴 뷰를 연결하는 URL 패턴.
    path('withdraw/<int:pk>', views.UserDeleteView.as_view(), name='delete'),

]
