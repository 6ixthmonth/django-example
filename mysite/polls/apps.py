from django.apps import AppConfig


class PollsConfig(AppConfig):
    """polls 앱을 설정 파일에 등록할 때 사용하는 앱 구성 클래스."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
