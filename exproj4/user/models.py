from django.db import models


class User(models.Model):
    """사용자를 표현하는 모델 클래스."""

    id = models.CharField(max_length=20, primary_key=True)
    pw = models.CharField(max_length=20)
    nm = models.CharField(max_length=20)

    def __str__(self) -> str:
        # 관리자 페이지에서 출력할 때 사용.
        return f"{self.nm}"

    def __repr__(self) -> str:
        # 파이썬 셸에서 출력할 때 사용.
        return f"{{ id: '{self.id}', nm: '{self.nm}' }}"
