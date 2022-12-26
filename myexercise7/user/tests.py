from django.test import TestCase

from .models import User


def create_user(id="tester", pw="1234", nm="검사자") -> User:
    """검사에 사용할 사용자를 생성하는 함수."""
    return User.objects.create(id=id, pw=pw, nm=nm)
