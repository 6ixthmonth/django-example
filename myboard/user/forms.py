from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """내장 폼 클래스인 UserCreationForm 클래스를 상속하여 구현한 사용자 정의 폼 클래스."""

    # 추가하고 싶은 필드가 있으면 클래스 변수 형태로 작성.
    # 실제로 이 필드의 데이터를 데이터베이스에 저장하는 등의 조작을 하려면 모델 클래스 또한 재정의 해야 한다.
    nickname = forms.CharField(label='별명')

    # Meta 클래스의 작성을 생략하면 상위 폼 클래스의 Meta 클래스를 사용한다.
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'nickname', 'first_name', 'last_name', 'email',)  # password1, password2 필드는 추가하지 않아도 자동으로 적용된다.


class CustomUserChangeForm(UserChangeForm):
    """내장 폼 클래스인 UserChangeForm 클래스를 상속하여 구현한 사용자 정의 폼 클래스."""

    nickname = forms.CharField(label='별명')

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'nickname', 'first_name', 'last_name', 'email')
