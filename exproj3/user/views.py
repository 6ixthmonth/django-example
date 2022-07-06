from django.http import HttpResponse


def create_user(request):
    """사용자 등록 뷰 함수"""

    return HttpResponse("사용자 등록 페이지")


def user_form(request):
    """로그인 뷰 함수"""

    context = """
        <h1>로그인 페이지</h1>
        <table>
            <tr>
                <th>ID</th>
                <td><input type='text'></td>
            </tr>
            <tr>
                <th>비밀번호</th>
                <td><input type='password'></td>
            </tr>
            <tr>
                <td colspan=2><input type='button' value='로그인'></td>
            </tr>
        </table>
    """

    return HttpResponse(context)
