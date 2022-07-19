from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User


def home(request):
    """홈 페이지로 이동하는 뷰 함수."""
    return render(request, 'user/home.html')


def user_create(request):
    """사용자 등록 관련 뷰 함수."""
    if request.method == "POST":
        # POST 방식으로 요청한 경우, 데이터베이스에 사용자 데이터를 저장한다.
        try:
            # 사용자가 입력한 사용자 데이터를 가져온다.
            user_id = request.POST['id']
            user_pw = request.POST['pw']
            user_pw_chk = request.POST['pw_chk']
            user_nm = request.POST['nm']

            if len(user_id) > 0 and len(user_pw) > 0 and user_pw == user_pw_chk and len(user_nm) > 0 and not User.objects.filter(pk=user_id).exists():
                # 조건을 만족하면 데이터베이스에 사용자 데이터를 저장하고 로그인 페이지로 리다이렉트 한다.
                User.objects.create(id=user_id, pw=user_pw, nm=user_nm)
                return HttpResponseRedirect(reverse('user:login'))
        except KeyError:
            pass
    # GET 방식으로 요청한 경우, 또는 조건을 만족하지 못하면 다시 사용자 등록 페이지로 이동한다.
    return render(request, 'user/user_create.html')


def user_login(request):
    """로그인 관련 뷰 함수."""
    if request.method == "POST":
        # POST 방식으로 요청한 경우, 데이터베이스로부터 사용자 데이터를 조회한다.
        try:
            # 사용자가 입력한 ID에 해당하는 사용자 데이터를 가져온다.
            login_user = User.objects.get(id=request.POST['id'])

            if login_user.pw == request.POST['pw']:
                # 조건을 만족하면 세션에 사용자 데이터를 저장하고 홈 화면으로 리다이렉트 한다.
                request.session['user_nm'] = login_user.nm
                return HttpResponseRedirect(reverse('home'))
        except (KeyError, User.DoesNotExist):
            pass
        # GET 방식으로 요청한 경우, 또는 조건을 만족하지 못하면 다시 로그인 페이지로 이동한다.
    return render(request, 'user/user_login.html')


def user_logout(request):
    """로그아웃 뷰 함수"""
    # 세션에 저장된 사용자 데이터를 삭제하고 홈 화면으로 리다이렉트 한다.
    del request.session['user_nm']
    return HttpResponseRedirect(reverse('home'))
