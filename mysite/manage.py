#!/usr/bin/env python
"""
관리 작업을 위한 장고의 명령 줄 유틸리티.

서버를 실행하거나 앱을 생성하는 등, 장고 프로젝트를 관리하기 위해 다양한 기능을 제공한다.
기능을 실행하려면 이 스크립트 파일을 명령어와 함께 명령 프롬프트에서 실행한다. ex) py manage.py runserver
"""


import os
import sys


def main():
    """관리 작업을 실행한다."""

    # 환경 설정 파일(mysite 폴더에 있는 settings.py 파일)을 적용한다.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

    try:
        # 입력된 명령어를 실행하기 위해서 필요한 함수를 불러온다.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 장고가 설치되어 있지 않거나 환경 변수에서 찾을 수 없을 때 오류를 발생시킨다.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 시스템 인수 형태로 입력된 명령어를 실행한다.
    execute_from_command_line(sys.argv)


# 이 스크립트가 실행되면 main() 함수를 실행한다.
if __name__ == '__main__':
    main()
