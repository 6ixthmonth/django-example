from django.urls import path

from . import views


urlpatterns = [
    path('', views.board_list),  # 게시판 URL 패턴.
]
