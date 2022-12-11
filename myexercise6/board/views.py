from django.shortcuts import render, get_object_or_404

from .models import Board


def board_list(request):
    """게시글 목록 뷰 함수."""
    board_list = Board.objects.order_by('-date')
    context = {
        'board_list': board_list,
    }
    return render(request, 'board/board_list.html', context)


def board_detail(request, board_number):
    """게시글 상세 뷰 함수."""
    board = get_object_or_404(Board, pk=board_number)
    context = {
        'board': board,
    }
    return render(request, 'board/board_detail.html', context)
