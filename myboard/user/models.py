from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    """내장 모델 클래스인 User 클래스를 상속하여 구현한 사용자 정의 모델 클래스."""

    password2 = models.CharField(max_length=128)  # 검증을 위해 추가한 비밀번호 확인 필드.
