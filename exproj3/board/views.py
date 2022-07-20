from django.http import HttpResponse


def board_list(request):
    """게시글 목록 뷰 함수."""
    return HttpResponse("게시글 목록")
