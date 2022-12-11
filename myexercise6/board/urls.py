from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('', views.board_list, name='list'),
    path('<int:board_number>/', views.board_detail, name='detail'),
]
