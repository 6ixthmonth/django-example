from django.urls import path

from . import views


urlpatterns = [
    path('', views.board_list),
    path('<int:board_number>', views.board_detail),
]
