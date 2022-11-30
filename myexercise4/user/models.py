from django.db import models


class User(models.Model):
    """사용자를 표현하는 모델 클래스."""

    id = models.CharField(max_length=20, primary_key=True)
    pw = models.CharField(max_length=20)
    nm = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{{ id: '{self.id}', nm: '{self.nm}' }}"
