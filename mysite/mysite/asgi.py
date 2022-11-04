"""
이 프로젝트에 대한 ASGI 구성.

ASGI 객체가 호출될 수 있도록 'application'이라는 이름의 모듈 수준 변수로 노출시킨다.

이 파일에 대한 더 많은 정보는 하단의 링크에서 확인할 수 있다.
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
