from django.http import HttpResponse


def create_user(request):
    """사용자 등록 뷰 함수"""

    return HttpResponse("사용자 등록 페이지")


def user_form(request):
    """로그인 뷰 함수"""

    context = "<h1>로그인 페이지</h1>"
    context += "<table>"
    context += "    <tr>"
    context += "        <th>ID</th>"
    context += "        <td><input type='text'></td>"
    context += "    </tr>"
    context += "    <tr>"
    context += "        <th>비밀번호</th>"
    context += "        <td><input type='password'></td>"
    context += "    </tr>"
    context += "    <tr>"
    context += "        <td><input type='button' value='로그인'></td>"
    context += "    </tr>"
    context += "</table>"

    return HttpResponse(context)
