from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from . import views


app_name = 'user'
urlpatterns = [

    # 로그인 뷰를 연결하는 URL 패턴. 내장 뷰를 사용하여 로그인 페이지로 이동하거나 로그인을 처리한다. 다음과 같은 인수를 전달할 수 있다.
    # # template_name
    # # # GET 요청을 처리할 때 응답할 템플릿 파일 이름. 기본 값은 'registration/login.html'.
    # # # 로그인 페이지 템플릿 파일 이름을 설정한다.
    # # next_page
    # # # POST 요청을 처리한 후 리다이렉트 할 URL 문자열 값. 기본 값은 '/accounts/profile/'.
    # # # 요청에 next 인수가 있으면 next 인수 값으로 리다이렉트 한다.
    path('login/', LoginView.as_view(template_name='user/login.html', next_page=reverse_lazy('home')), name='login'),

    # 로그아웃 뷰를 연결하는 URL 패턴. 내장 뷰를 사용하여 로그아웃을 처리한다. 다음의 인수들 중 하나를 설정할 수 있다.
    # # template_name
    # # # 로그아웃 처리 후 응답할 템플릿 파일 이름. 기본 값은 'registration/logged_out.html'.
    # # # 장고 설치 시 기본적으로 제공되는 템플릿 파일이기 때문에 이 인수를 생략해도 정상적으로 동작한다.
    # # next_page
    # # # 로그아웃 처리 후 리다이렉트할 URL. 문자열 값. 기본 값은 None.
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),

    # 사용자 등록 뷰를 연결하는 URL 패턴.
    path('join/', views.UserCreateView.as_view(), name='create'),

    # 사용자 정보 수정 뷰를 연결하는 URL 패턴.
    path('edit/<int:pk>', views.UserUpdateView.as_view(), name='update'),

    # 사용자 탈퇴 뷰를 연결하는 URL 패턴.
    path('withdraw/<int:pk>', views.UserDeleteView.as_view(), name='delete'),

]
