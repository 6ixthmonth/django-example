from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    path('', views.BoardListView.as_view(), name='list'),
    path('<int:pk>/', views.BoardDetailView.as_view(), name='detail'),
]
