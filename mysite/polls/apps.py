"""
앱 구성 클래스를 작성하는 파일.

앱 구성 클래스는 앱을 생성하면 자동으로 작성되기 때문에 일반적인 상황에서 직접 작성하거나 수정할 일은 거의 없다.
작성된 클래스를 settings.py 파일의 INSTALLED_APPS 변수에 등록하면 이 프로젝트에서 해당 앱을 인식하고 동작시킬 수 있다.
"""


from django.apps import AppConfig


class PollsConfig(AppConfig):
    """polls 앱을 설정 파일에 등록할 때 사용하는 앱 구성 클래스."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
