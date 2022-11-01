from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('', views.board_list, name='list'),  # 게시판 URL 패턴.
    path('<int:board_number>/', views.board_detail, name='detail'),  # 게시글 상세 URL 패턴.
]
