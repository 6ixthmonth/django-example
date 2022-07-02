from django.db import models


class User(models.Model):
    """사용자 클래스"""
    id = models.CharField(max_length=20, primary_key=True)  # 사용자 ID
    pw = models.CharField(max_length=20)  # 사용자 비밀번호
    nm = models.CharField(max_length=20)  # 사용자 이름

    def __str__(self) -> str:
        return f"{{ id: '{self.id}', nm: '{self.nm}' }}"
