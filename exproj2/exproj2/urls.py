from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # 사용자 앱 URL 패턴.
    path('board/', include('board.urls')),  # 게시판 앱 URL 패턴.
]
