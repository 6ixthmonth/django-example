from django.urls import path

from . import views


urlpatterns = [
    path('', views.board_list)  # 게시글 목록.
]
