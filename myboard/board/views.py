from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

import board

from .models import Board, Reply
from .forms import BoardForm, ReplyForm


class BoardListView(ListView):
    """게시글 목록 뷰."""
    model = Board
    template_name = "board/board_list.html"

    def get_queryset(self):
        return Board.objects.order_by('-date')


class BoardDetailView(DetailView):
    """게시글 상세 뷰."""
    model = Board
    template_name = "board/board_detail.html"


class BoardCreateView(LoginRequiredMixin, CreateView):
    """게시글 작성 뷰."""

    # LoginRequiredMixin
    login_url = reverse_lazy('user:login')
    # redirect_field_name = 'redirect_to'

    form_class = BoardForm
    template_name = "board/board_form.html"
    success_url = reverse_lazy('board:list')

    def form_valid(self, form) -> HttpResponse:
        if form.is_valid():
            board = form.save(commit=False)
            board.user = self.request.user
            return super(BoardCreateView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form) -> HttpResponse:
        return super().form_invalid(form)


def reply_create(request):
    content = request.POST['content']
    user = request.user
    board_number = request.POST['board_number']

    Reply.objects.create(content=content, user=user, board_id=board_number)

    return redirect('board:detail', pk=board_number)
