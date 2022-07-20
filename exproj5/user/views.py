from django.shortcuts import render


def home(request):
    """홈 페이지로 이동하는 뷰 함수."""
    return render(request, 'user/home.html')


def user_create(request):
    """사용자 등록 뷰 함수."""
    return render(request, 'user/user_create.html')


def user_login(request):
    """로그인 뷰 함수."""
    return render(request, 'user/user_login.html')
