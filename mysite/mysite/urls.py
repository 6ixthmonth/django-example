"""
이 프로젝트의 URL 구성 파일.

`urlpatterns` 목록은 URL을 뷰로 전달한다. 더 많은 정보는 하단의 링크를 통해 확인할 수 있다.
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
예시:
함수 뷰
    1. import를 추가한다:  from my_app import views
    2. urlpatterns에 URL을 추가한다:  path('', views.home, name='home')
클래스 기반 뷰
    1. import를 추가한다:  from my_app import views
    2. urlpatterns에 URL을 추가한다:  path('', Home.as_view(), name='home')
다른 URL 구성 파일 포함시키기
    1. include() 함수를 불러온다:  from django.urls import include, path
    2. urlpatterns에 URL을 추가한다:  path('blog/', include('blog.urls'))


이 파일은 최상위 URL 구성 파일(root URL configuration file, root URLconf file)로써 URL 양식을 기록한다.
URL 양식은 클라이언트에서 요청을 보낼 때 사용할 URL과, 서버에서 이를 처리하고 응답할 뷰를 연결한다.
URL 양식은 path() 함수를 사용해서 작성하고 urlpatterns 목록 변수에 등록한다.
"""


from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # 투표 앱 관련 URL 양식.
    # 'polls/*' 문자열과 같은 형태의 URL을 통해 요청이 발생하면,
    # polls 앱의 URL 구성 파일(polls 폴더에 위치한 urls.py 파일)을 통해 처리한다.
    path('polls/', include('polls.urls')),

    # 관리자 앱 관련 URL 양식.
    path('admin/', admin.site.urls),
]
