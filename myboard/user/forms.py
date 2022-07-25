from django import forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    # 추가하고싶은 폼 필드가 있으면 여기에 클래스 변수 추가

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields  # 추가한 필드를 여기에 리스트로 추가
