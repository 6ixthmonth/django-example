from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


class UserCreateView(CreateView):
    """
    사용자 등록 뷰.
    내장 뷰 클래스인 CreateView를 상속하여 구현한 사용자 정의 뷰 클래스.
    GET 요청 시, 사용자 등록 페이지로 이동하며,
    POST 요청 시, 전달받은 신규 사용자 데이터를 저장한다.
    """

    # CreateView가 동작하려면 모델과 필드를 각각 따로 설정하거나, 폼 클래스를 이용해서 한꺼번에 설정해야 한다.

    # 1. 이 뷰에서 다룰 모델 클래스와, 템플릿에서 다룰 필드 목록을 각각 따로 설정.
    # from django.contrib.auth.models import User
    # model = User  # 이 뷰에서 다룰 모델 클래스. 여기서는 내장 클래스인 User 클래스를 설정한다.
    # fields = ['username', 'password']  # 템플릿에서 다룰 필드 목록. User 클래스가 가진 필드 중 원하는 대상을 작성한다.

    # 1-2. 내장 모델 클래스의 필드 외 다루고 싶은 필드가 있으면 사용자 정의 모델 클래스를 사용한다.
    # from .models import CustomUser
    # model = CustomUser  # 내장 모델 클래스인 User 클래스를 상속하여 구현한 사용자 정의 모델 클래스.
    # fields = ['username', 'password', 'password2']

    # 2. 폼 클래스를 이용해서 한꺼번에 설정하는 방법.
    # from django.contrib.auth.forms import UserCreationForm
    # form_class = UserCreationForm  # 이 뷰에서 다룰 폼 클래스. 폼 클래스에 작성되어 있는 모델과 필드가 자동으로 적용된다. 내장 폼 클래스인 UserCreationForm의 경우, User 모델과 ('username', 'password1', 'password2') 필드를 가지고 있다.

    # 2-2. 내장 폼 클래스의 필드 외 다루고 싶은 필드가 있으면 사용자 정의 폼 클래스를 사용한다.
    from .forms import CustomUserCreationForm
    form_class = CustomUserCreationForm  # 내장 폼 클래스인 UserCreationForm 클래스를 상속하여 구현한 사용자 정의 폼 클래스.

    # GET 요청 시 응답할 템플릿 파일의 경로 및 파일 이름.
    template_name = "user/user_form.html"  # User 모델을 사용하는 CreateView이기 때문에 기본 값은 'auth/user_form.html'.

    # POST 요청 처리 후 리다이렉트할 URL.
    # success_url = reverse('home')  # 클래스 기반 뷰에서는 URL 구성 파일이 아직 로딩되지 않아 reverse() 함수를 사용할 수 없다.
    success_url = reverse_lazy('home')  # 대신 reverse_lazy() 함수를 사용한다..

    
    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['user_type'] = '등록'
        return context


class UserUpdateView(UpdateView):
    """사용자 정보 변경 뷰."""

    from .forms import CustomUserChangeForm
    form_class = CustomUserChangeForm

    template_name = "user/user_form.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['user_type'] = '정보 변경'
        return context


class UserDeleteView(DeleteView):
    """사용자 탈퇴 뷰."""

    from django.contrib.auth.models import User
    model = User
    success_url = reverse_lazy('home')
