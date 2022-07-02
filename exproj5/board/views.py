from django.shortcuts import render

from .models import Board, Reply


def board_list(request):
    """게시글 목록 뷰 함수"""

    context = {"board_list": Board.objects.order_by('-date')}

    return render(request, 'board/list.html', context)
