from django.db import models


class User(models.Model):
    """사용자를 표현하는 모델 클래스."""

    id = models.CharField(max_length=20, primary_key=True)  # ID.
    pw = models.CharField(max_length=20)  # 비밀번호.
    nm = models.CharField(max_length=20)  # 이름.

    def __str__(self) -> str:
        return f"{{ id: '{self.id}', nm: '{self.nm}' }}"
