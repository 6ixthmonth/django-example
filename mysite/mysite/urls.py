"""
기본 URL 구성(URLconf) 파일.

urlpatterns 변수를 통해 요청 URL과 이를 처리할 view를 기록할 수 있다.
path() 함수에 인식시킬 요청 URL 문자열 값과 이를 처리할 view 함수(또는 클래스)를 작성한다.

하단의 링크를 통해 장고에서 요청을 처리하는 절차에 대해 자세히 확인할 수 있다.
https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""


from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('polls/', include('polls.urls')), # 투표 앱 관련 URL 패턴. `[rootpath]/polls/*` 와 같은 형태의 요청이 들어오면 polls 폴더의 urls.py 파일을 통해 처리한다.
    path('admin/', admin.site.urls), # 관리자 페이지로 이동하는 URL 패턴.
]
