from django.db import models


class User(models.Model):
    """사용자 클래스"""
    user_id = models.CharField(max_length=20, primary_key=True)  # 사용자 ID
    user_pw = models.CharField(max_length=20)  # 사용자 비밀번호
    user_nm = models.CharField(max_length=20)  # 사용자 이름

    def __str__(self) -> str:
        return f"{self.user_nm}"

    def __repr__(self) -> str:
        return f"{{ user_id: '{self.user_id}', user_nm: '{self.user_nm}' }}"
