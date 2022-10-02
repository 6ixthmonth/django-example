from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


class UserCreateView(CreateView):
    """
    사용자 등록 뷰.
    내장 뷰 클래스인 CreateView를 상속하여 구현한 사용자 정의 뷰.
    GET 요청 시, 사용자 등록 페이지로 이동하며, POST 요청 시, 전달받은 신규 사용자 데이터를 저장한다.
    """

    # CreateView는 모델과 필드를 각각 따로 등록하거나, 폼을 이용해서 한꺼번에 등록해서 사용한다.

    # 1. 이 뷰에서 다룰 모델 클래스와, 웹 페이지에 표시할 필드 목록을 각각 따로 정의하는 방법.
    # from django.contrib.auth.models import User
    # model = User  # 이 뷰에서 다룰 모델 클래스. 여기서는 빌트-인 사용자 클래스인 User 클래스를 적용한다.
    # fields = ['username', 'password']  # 웹 페이지에서 입력받기 위해 표시할 필드 목록. User 클래스가 가진 필드 중 표시하기 원하는 걸 골라서 작성한다.

    # 1-2. 빌트인 모델 클래스의 필드 외 표시하고 싶은 필드가 있으면 사용자 정의 모델 클래스를 사용한다.
    # from .models import CustomUser
    # model = CustomUser  # 빌트-인 모델 클래스인 User 클래스를 상속하여 구현한 사용자 정의 모델 클래스.
    # fields = ['username', 'password', 'password2']

    # 2. 이 뷰에서 다룰 모델과 필드를 폼 클래스로 한꺼번에 정의하는 방법.
    # from django.contrib.auth.forms import UserCreationForm
    # form_class = UserCreationForm  # 이 뷰에서 다룰 폼 클래스. 폼에 작성되어 있는 모델과 필드가 자동으로 적용된다. 빌트-인 폼 클래스인 UserCreationForm의 경우, User 모델과 ('username', 'password1', 'password2') 필드를 가지고 있다.

    # 2-2. 기존 폼 클래스의 필드 외 표시하고 싶은 필드가 있으면 사용자 정의 폼 클래스를 사용한다.
    from .forms import CustomUserCreationForm
    form_class = CustomUserCreationForm  # 빌트-인 폼 클래스인 UserCreationForm 클래스를 상속하여 구현한 사용자 정의 폼 클래스.

    # GET 요청 시 이동할 웹 문서의 경로 및 파일명.
    template_name = "user/user_form.html"  # User 모델을 사용하는 CreateView이기 때문에 기본 값은 'auth/user_form.html'.

    # POST 요청 처리 후 리다이렉트할 URL.
    # success_url = reverse('home')  # URLconf 파일이 아직 로딩되지 않아 오류 발생.
    success_url = reverse_lazy('home')  # 파일 로딩 후 적용.

    
    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['user_type'] = '등록'
        return context


class UserUpdateView(UpdateView):
    """사용자 정보 변경 뷰."""

    from django.contrib.auth.models import User
    model = User
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
