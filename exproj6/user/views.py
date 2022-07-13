from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User


def home(request):
    """홈 화면 이동"""

    return render(request, 'user/home.html')


def create(request):
    """사용자 등록 뷰 함수"""

    if request.method == "GET":
        # GET 방식으로 요청한 경우 사용자 등록 페이지로 이동
        return render(request, 'user/create.html')
    else:
        try:
            # 사용자가 입력한 사용자 데이터를 가져옴
            user_id = request.POST['id']
            user_pw = request.POST['pw']
            user_pw_chk = request.POST['pw_chk']
            user_nm = request.POST['nm']

            if len(user_id) > 0 and len(user_pw) > 0 and user_pw == user_pw_chk and len(user_nm) > 0 and not User.objects.filter(pk=user_id).exists():
                # 조건을 만족하면 데이터베이스에 사용자 데이터를 저장하고 로그인 페이지로 이동
                User(id=user_id, pw=user_pw, nm=user_nm).save()
                return HttpResponseRedirect(reverse('user:form'))
        except KeyError:
            pass
        # 조건을 만족하지 못하면 다시 사용자 등록 페이지로 이동
        return HttpResponseRedirect(reverse('user:create'))


def form(request):
    """로그인 뷰 함수"""

    if request.method == "GET":
        # GET 방식으로 요청한 경우 로그인 페이지로 이동
        return render(request, 'user/form.html')
    else:
        try:
            # 사용자가 입력한 ID에 해당하는 사용자 데이터를 가져옴
            login_user = User.objects.get(id=request.POST['id'])

            if login_user.pw == request.POST['pw']:
                # 조건을 만족하면 세션에 사용자 데이터를 저장하고 홈 화면으로 이동
                request.session['user_nm'] = login_user.nm
                return HttpResponseRedirect(reverse('home'))
        except User.DoesNotExist:
            pass
        # 조건을 만족하지 못하면 다시 로그인 페이지로 이동
        return HttpResponseRedirect(reverse('user:form'))


def signout(request):
    """로그아웃 뷰 함수"""

    # 세션에 저장된 사용자 데이터를 삭제하고 홈 화면으로 이동
    del request.session['user_nm']

    return HttpResponseRedirect(reverse('home'))
