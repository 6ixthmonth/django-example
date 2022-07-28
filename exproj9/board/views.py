from django.views import generic

from .models import Board


class ListView(generic.ListView):
    # template_name = "board/board_list.html"  # 기본 값: "<앱 이름>/lower(<모델 이름>)_list.html"
    # context_object_name = "board_list"  # 기본 값: "object_list" 또는 "lower(<모델 이름>)_list"

    def get_queryset(self):
        return Board.objects.order_by('-date')


class DetailView(generic.DetailView):
    model = Board
    # template_name = "board/board_detail.html"  # 기본 값: "<앱 이름>/lower(<모델 이름>)_detail.html"
    # context_object_name = "board"  # 기본 값: "object" 또는 "lower(<모델 이름>)""
    pk_url_kwarg = "board_number"  # 기본 값: "pk"
