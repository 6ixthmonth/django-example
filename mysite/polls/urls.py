"""
polls 앱에서 사용하는 하위 URL 설정 파일. URL 양식을 작성하는 파일이다.
"""


from django.urls import path

from . import views


# 이 앱에서 사용할 이름공간(namespace) 설정.
app_name = 'polls'

# 함수 뷰 사용.
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# 클래스 기반 뷰 사용.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
