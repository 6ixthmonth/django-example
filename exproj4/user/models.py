from django.db import models


class User(models.Model):
    """사용자를 표현하는 모델 클래스."""

    id = models.CharField(max_length=20, primary_key=True)  # ID.
    pw = models.CharField(max_length=20)  # 비밀번호.
    nm = models.CharField(max_length=20)  # 이름.

    # 관리자 페이지에서 User 객체 출력 시 사용.
    def __str__(self) -> str:
        return f"{self.nm}"

    # 파이썬 셸에서 User 객체 출력 시 사용.
    def __repr__(self) -> str:
        return f"{{ id: '{self.id}', nm: '{self.nm}' }}"
