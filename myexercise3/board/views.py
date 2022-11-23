from django.http import HttpResponse


def board_list(request):
    """게시판 뷰 함수."""
    return HttpResponse("게시판")
