from django.contrib import admin
from django.urls import path, include

from user import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('user/', include('user.urls')),  # 사용자 관련 앱 (사용자 등록, 로그인 등)
    path('board/', include('board.urls')),  # 게시판 관련 앱 (게시글 목록 등)
]
