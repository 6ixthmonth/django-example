from django.http import HttpResponse


def user_create(request):
    """사용자 등록 뷰 함수."""
    return HttpResponse("사용자 등록")


def user_login(request):
    """로그인 뷰 함수."""
    content = """
        <h1>로그인</h1>
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
                <td colspan='2'><input type='button' value='로그인'></td>
            </tr>
        </table>
        <a href='/user/join/'>사용자 등록</a>
    """
    return HttpResponse(content)
