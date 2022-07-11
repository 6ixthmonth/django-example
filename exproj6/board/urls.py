from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),  # 게시글 목록
    path('<int:board_number>/', views.DetailView.as_view(), name='detail') # 게시글 상세
]
