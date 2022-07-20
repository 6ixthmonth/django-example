from django.shortcuts import render, get_object_or_404

from .models import Board


def board_list(request):
    """게시글 목록 뷰 함수."""
    # 데이터베이스에서 모든 게시글 데이터를 날짜 역순으로 가져와서 웹 페이지로 전달한다.
    board_list = Board.objects.order_by('-date')
    context = {
        'board_list': board_list,
    }
    return render(request, 'board/board_list.html', context)


def board_detail(request, board_number):
    """게시글 상세 뷰 함수."""
    # 데이터베이스에서 특정 게시글 데이터를 가져와서 웹 페이지로 전달한다.
    board = get_object_or_404(Board, pk=board_number)  # 전달받은 게시글 번호에 해당하는 데이터가 없으면 404 오류를 발생시킨다.
    context = {
        'board': board,
    }
    return render(request, 'board/board_detail.html', context)
