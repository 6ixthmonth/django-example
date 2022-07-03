from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('list/', views.board_list, name='list'),  # 게시글 목록
    path('<int:board_number>/', views.board_detail, name='detail') # 게시글 상세
]
