from tabnanny import verbose
from django import forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """빌트-인 폼 클래스인 UserCreationForm 클래스를 상속하여 구현한 사용자 정의 폼 클래스."""

    # 추가하고 싶은 필드가 있으면 여기에 클래스 변수 추가.
    # 실제로 이 필드의 데이터를 저장하려면 model을 재정의 해야 한다.
    nickname = forms.CharField(label='닉네임')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')  # UserCreationForm의 기본 필드 ('username',) 외에 추가로 구성하고 싶은 필드 작성(password1, password2는 자동으로 적용되는 항목).


class CustomUserChangeForm(UserChangeForm):
    """빌트-인 폼 클래스인 UserChangeForm 클래스를 상속하여 구현한 사용자 정의 폼 클래스."""

    nickname = forms.CharField(label='닉네임')

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
