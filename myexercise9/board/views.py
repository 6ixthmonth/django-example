from django.views.generic import ListView, DetailView

from .models import Board


class BoardListView(ListView):
    model = Board
    ordering = '-date'


class BoardDetailView(DetailView):
    model = Board
