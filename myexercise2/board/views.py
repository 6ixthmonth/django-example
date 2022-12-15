from django.http import HttpResponse


def board_list(request):
    """게시판 뷰."""
    return HttpResponse("게시판")

def board_detail(request, board_number):
    """게시글 상세 뷰."""
    print("조회하고자 하는 게시글 번호: %d" % board_number)
    return HttpResponse("%d번 게시글 상세" % board_number)
