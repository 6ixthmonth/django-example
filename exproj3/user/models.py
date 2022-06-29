from django.db import models


class User(models.Model):
    """사용자 클래스"""
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    user_nm = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{{ user_id: {self.user_id}, user_nm: {self.user_nm} }}"
