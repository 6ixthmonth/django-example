from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Board, Reply
from .forms import BoardForm


BOARD_PER_PAGE = 10  # 게시글 목록 페이지에서 한 페이지 당 표시할 게시글 수.


class BoardListView(ListView):
    """게시글 목록 뷰 클래스."""

    paginate_by = BOARD_PER_PAGE  # 페이징 처리 설정.
    template_name = "board/board_list.html"

    def get_queryset(self):
        search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')
        if search_type and search_word:
            if search_type == 'title':
                return Board.objects.filter(title__icontains=search_word).order_by('-date')
            elif search_type == 'content':
                return Board.objects.filter(content__icontains=search_word).order_by('-date')
            elif search_type == 'username':
                return Board.objects.filter(user__username__icontains=search_word).order_by('-date')
            else:
                pass
        return super().get_queryset()  # 검색을 요청한 경우가 아니면 모든 게시글을 가져와서 반환한다.
    
    def get_context_data(self, **kwargs):
        # 검색 기능에 페이징 기능을 적용하기 위해 전달받은 검색 종류, 검색어를 다시 응답한다.
        context = super(BoardListView, self).get_context_data(**kwargs)
        search_type = self.request.GET.get('search_type', '')  # 전달받은 검색 종류를 가져온다.
        search_word = self.request.GET.get('search_word', '')  # 전달받은 검색어를 가져온다.
        if search_type and search_word:
            context['search_type'] = search_type  # 콘텍스트에 검색 종류를 입력하여 템플릿으로 전달한다.
            context['search_word'] = search_word  # 콘텍스트에 검색어를 입력하여 템플릿으로 전달한다.
        return context
    

class BoardDetailView(DetailView):
    """게시글 상세 뷰. model, template_name 속성 외에 추가로 작성할 속성은 없으며, 전달받은 기본 키 값(Board 객체의 number 필드)에 해당하는 Board 객체를 찾아서 반환한다."""

    model = Board
    template_name = "board/board_detail.html"


class BoardCreateView(LoginRequiredMixin, CreateView):
    """게시글 작성 뷰. 기본적으로 form_class, template_name, success_url 속성만 작성해도 되지만 파일 업로드 기능 등을 위해 추가 속성을 작성하고 함수를 오버라이딩 한다."""

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

    def form_valid(self, form):
        # 전달받은 양식이 유효한 경우 실행되는 함수. 기본적으로 success_url로 리다이렉트 할 뿐인 함수로 구현되어 있다.

        # form 매개변수와 주요 속성.
        # form: board.forms.BoardForm 객체. 페이지에서 전달한 양식 데이터와 각종 메타 데이터를 가지고 있다.
        # form.instance: board.models.Board 객체. 양식 데이터를 모델화한 객체.
        # form.data: 양식과 관련된 모든 데이터를 담은 사전 객체. 일반적인 경우 사용하지 않는다.
        # form.cleaned_data: 양식에 입력된 데이터만 담은 사전 객체. form.cleaned_data['title'] 등의 형태로 특정 입력 필드에 대한 데이터만 순수하게 추출할 때 사용한다.
        # form.save(): 양식으로 전달된 데이터를 데이터베이스에 저장할 때 사용하는 함수. 저장된 모델 객체를 반환한다.

        # 파일을 업로드한 경우.
        if self.request.FILES:
            # form.instance.attached_file = self.request.FILES['upload_file']  # 전달받은 파일 객체를 모델 객체에 저장한다.
            upload_file = self.request.FILES['upload_file']  # 전달 받은 파일 객체.
            form.instance.original_file_name = upload_file.name  # 원본 파일 이름 설정.
            form.instance.attached_file = upload_file  # 첨부 파일 설정.

        form.instance.user = self.request.user  # 전달받은 양식 데이터(=Board 모델 객체)의 게시글 작성자 항목에 현재 로그인 한 사용자를 입력한다.
        form.save(commit=True)  # 양식 데이터를 데이터베이스에 저장한다.

        # return super().form_valid(form)  # success_url로 리다이렉트 하는 기존 구현.
        # return redirect(reverse_lazy('board:detail', args=(form.instance.number,)))  # 저장 후 생성된 게시글 번호 PK값을 가지고 게시글 상세 페이지로 리다이렉트.
        return redirect(reverse_lazy('board:detail', kwargs={'pk': form.instance.number}))  # 생성된 게시글의 상세 페이지로 리다이렉트.

    def form_invalid(self, form):
        # 전달받은 양식이 유효하지 않는 경우 실행되는 함수.
        return super().form_invalid(form)


class BoardUpdateView(UpdateView):
    """게시글 수정 뷰."""

    model = Board  # model 또는 query_set 설정 필수.
    form_class = BoardForm  # fields 대신 사용.
    template_name = "board/board_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_type'] = '수정'  # board_form.html 템플릿을 재활용하기 위해, 이 응답이 어떤 게시글 관련 동작을 위한 것인지 콘텍스트에 추가.
        return context

    def get_success_url(self) -> str:
        # return reverse_lazy('board:detail', args=(self.kwargs['pk'],))  # 게시글 수정에 성공한 경우, 게시글 상세 페이지로 이동하기 위해 해당 URL을 리턴.
        return reverse_lazy('board:detail', args=(self.object.number,))


class BoardDeleteView(DeleteView):
    """게시글 삭제 뷰."""

    model = Board
    success_url = reverse_lazy('board:list')


@login_required(login_url=reverse_lazy('user:login'))  # 이 함수 뷰에 로그인 한 사용자만 접근할 수 있도록 만드는 데코레이터.
def reply_create(request, board_number):
    """댓글 작성 뷰."""
    if request.method == 'POST':
        content = request.POST['content']  # 양식을 통해 전달받은 댓글 내용.
        user = request.user  # 현재 로그인 한 유저.
        Reply.objects.create(content=content, user=user, board_id=board_number)  # 전달받은 데이터를 이용해서 댓글 객체를 생성하고 데이터베이스에 저장한다.
    return redirect('board:detail', pk=board_number)  # 원본 게시글 상세 페이지로 리다이렉트 한다.


def file_download(request, board_number):
    """파일 다운로드 뷰."""
    board = Board.objects.get(pk=board_number)
    attached_file = board.attached_file  # 첨부 파일.
    original_file_name = board.original_file_name  # 원본 파일 이름.

    response = FileResponse(attached_file)  # 파일을 다운로드 하기 위한 응답 객체 생성.
    response['Content-Disposition'] = 'attachment; filename=%s' % original_file_name  # 원본 파일 이름 설정.

    return response
