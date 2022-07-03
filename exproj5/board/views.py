from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Board, Reply


def board_list(request):
    """게시글 목록 뷰 함수"""

    context = {
        'board_list': Board.objects.order_by('-date'),
    }

    return render(request, 'board/list.html', context)

def board_detail(request, board_number):
    """게시글 상세 뷰 함수"""

    board = get_object_or_404(Board, pk=board_number)
    reply_list = Reply.objects.filter(board_id=board_number)
    context = {
        'board': board,
        'reply_list': reply_list,
    }

    return render(request, 'board/detail.html', context)
