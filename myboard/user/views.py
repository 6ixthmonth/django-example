from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from .forms import CustomUserCreationForm


class UserCreateView(CreateView):
    model = User
    # fields = ['username', 'password']  # 웹 페이지에 렌더링할 필드 목록, form_class와 중복 적용 불가.
    form_class = UserCreationForm  # 웹 페이지에 렌더링할 폼. fields와 중복 적용 불가.
    # form_class = CustomUserCreationForm
    template_name = "user/user_form.html"  # template_name='auth/user_form.html' # User 모델을 사용하는 CreateView이기 때문.

    def get_success_url(self) -> str:
        return reverse_lazy('home')
