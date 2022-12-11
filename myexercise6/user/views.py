from django.http import HttpResponse


def user_create(request):
    """사용자 등록 뷰 함수."""
    return render(request, 'user/user_create.html')


def user_login(request):
    """로그인 뷰 함수."""
    return render(request, 'user/user_login.html')
