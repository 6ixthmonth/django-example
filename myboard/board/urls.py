from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('', views.BoardListView.as_view(), name="list"),  # 게시글 목록.
    path('<int:pk>/', views.BoardDetailView.as_view(), name="detail"),  # 게시글 상세.
    path('write/', views.BoardCreateView.as_view(), name='create'),  # 게시글 작성.
    path('<int:pk>/edit/', views.BoardUpdateView.as_view(), name='update'),  # 게시글 수정.
    # 게시글 삭제.
    path('<int:board_number>/reply/write', views.reply_create, name='reply_create'),  # 댓글 작성.
    # 댓글 수정.
    # 댓글 삭제.
]
