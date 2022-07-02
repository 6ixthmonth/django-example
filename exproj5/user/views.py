from django.shortcuts import render


def home(request):
    """홈 화면 이동"""

    return render(request, 'user/home.html')


def create_user(request):
    """사용자 등록 뷰 함수"""

    return render(request, 'user/create.html')


def user_form(request):
    """로그인 뷰 함수"""

    return render(request, 'user/form.html')
