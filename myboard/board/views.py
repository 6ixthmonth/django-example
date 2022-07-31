from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Board, Reply
from .forms import BoardForm


BOARD_PER_PAGE = 10  # 한 페이지 당 게시글 수.


class BoardListView(ListView):
    """게시글 목록 뷰."""

    model = Board
    ordering = '-date'  # 정렬 기준 열 이름. 게시글 작성일 역순(최신 글 우선)으로 지정.
    paginate_by = BOARD_PER_PAGE  # 페이징 처리 시 한 페이지 당 게시글 수.
    template_name = "board/board_list.html"

    def get_queryset(self):
        # 검색 기능 구현을 위해 게시글을 가져오는 함수를 오버라이딩 한다.
        search_type = self.request.GET.get('search_type', '')  # 검색 종류
        search_word = self.request.GET.get('search_word', '')  # 검색어
        if search_word:
            if search_type == 'title':
                print('count:', Board.objects.filter(title__icontains=search_word).count())
                return Board.objects.filter(title__icontains=search_word).order_by('-date')
            elif search_type == 'content':
                print('count:', Board.objects.filter(content__icontains=search_word).count())
                return Board.objects.filter(content__icontains=search_word).order_by('-date')
            elif search_type == 'username':
                print('count:', Board.objects.filter(user__username__icontains=search_word).count())
                return Board.objects.filter(user__username__icontains=search_word).order_by('-date')
            else:
                pass
        print('else execute')
        return super().get_queryset()

class BoardDetailView(DetailView):
    """게시글 상세 뷰."""

    model = Board
    template_name = "board/board_detail.html"


class BoardCreateView(LoginRequiredMixin, CreateView):
    """게시글 작성 뷰."""

    # LoginRequiredMixin: 이 클래스 뷰에 로그인 한 사용자만 접근할 수 있도록 만드는 Mixin 클래스. 로그인 하지 않고 요청을 시도하면 지정된 URL로 리다이렉트 한다.
    login_url = reverse_lazy('user:login')  # 로그인 하지 않은 사용자가 요청한 경우 리다이렉트 할 URL. 즉, 로그인 페이지의 URL을 작성한다. 기본 값은 '/accounts/login/'.
    # redirect_field_name = 'next'  # 로그인 후 리다이렉트 할 URL 값을 담은 변수의 이름. 보통 로그인 후 이전 페이지로 이동하기 위해 사용한다. 기본 값은 'next'.

    form_class = BoardForm
    template_name = "board/board_form.html"
    # success_url = reverse_lazy('board:list')  # 게시글 작성 후 이동할 URL. 작성된 게시글 상세 페이지로 동적으로 이동할 것이기 때문에 주석 처리.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_type'] = '작성'  # board_form.html 템플릿을 재활용하기 위해, 이 응답이 어떤 게시글 관련 동작을 위한 것인지 콘텍스트에 추가.
        return context

    def form_valid(self, form) -> HttpResponse:
        # form_valid(self, form): 전달받은 양식이 유효한 경우 실행되는 함수. 기본적으로 success_url로 리다이렉트 할 뿐인 함수로 구현되어 있다.

        # form 매개변수와 주요 특징.
        # form: board.forms.BoardForm 객체. 페이지에서 전달한 양식 데이터와 각종 메타 데이터를 가지고 있다.
        # form.instance: board.models.Board 객체. 양식 데이터를 모델화한 객체.
        # form.data: 양식과 관련된 모든 데이터를 담은 사전 객체. 일반적인 경우 사용하지 않는다.
        # form.cleaned_data: 양식에 입력된 데이터만 담은 사전 객체. form.cleaned_data['title'] 등의 형태로 특정 입력 필드에 대한 데이터만 순수하게 추출할 때 사용.
        # form.save(): 양식으로 전달된 데이터를 데이터베이스에 저장할 때 사용하는 함수. 저장된 모델 객체를 반환한다.

        form.instance.user = self.request.user  # 전달받은 양식 데이터(=Board 모델 객체)의 게시글 작성자 항목에 현재 로그인 한 사용자를 입력한다.
        form.save(commit=True)  # 양식 데이터를 데이터베이스에 저장한다.

        # return super().form_valid(form)  # success_url로 리다이렉트 하는 기존 구현.
        # return redirect(reverse_lazy('board:detail', args=(form.instance.number,)))  # 저장 후 생성된 게시글 번호 PK값을 가지고 게시글 상세 페이지로 리다이렉트.
        return redirect(reverse_lazy('board:detail', kwargs={'pk': form.instance.number}))  # 게시글 상세 페이지로 리다이렉트.

    def form_invalid(self, form) -> HttpResponse:
        # 전달받은 양식이 유효하지 않는 경우 실행되는 함수.
        return super().form_invalid(form)


@login_required(login_url=reverse_lazy('user:login'))  # 이 함수 뷰에 로그인 한 사용자만 접근할 수 있도록 만드는 데코레이터.
def reply_create(request, board_number):
    """댓글 작성 뷰."""
    if request.method == 'POST':
        content = request.POST['content']
        user = request.user
        Reply.objects.create(content=content, user=user, board_id=board_number)  # 전달받은 데이터를 이용해서 댓글 객체를 생성하고 데이터베이스에 저장한다.
    return redirect('board:detail', pk=board_number)  # 원본 게시글 상세 페이지로 리다이렉트 한다.


class BoardUpdateView(UpdateView):
    """게시글 수정 뷰."""

    model = Board  # model 또는 query_set 필수.
    form_class = BoardForm  # fields 대신 사용.
    template_name = "board/board_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_type'] = '수정'  # board_form.html 템플릿을 재활용하기 위해, 이 응답이 어떤 게시글 관련 동작을 위한 것인지 콘텍스트에 추가.
        return context

    def get_success_url(self) -> str:
        # 게시글 수정에 성공한 경우, 게시글 상세 페이지로 이동하기 위해 해당 URL을 리턴.
        # return reverse_lazy('board:detail', args=(self.kwargs['pk'],))
        return reverse_lazy('board:detail', args=(self.object.number,))


class BoardDeleteView(DeleteView):
    """게시글 삭제 뷰."""

    model = Board
    # template_name = "TEMPLATE_NAME"  # 기본 값: 'board/board_confirm_delete.html'
    success_url = reverse_lazy('board:list')
