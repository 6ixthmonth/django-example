from dataclasses import field, fields
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView

from .models import Board, Reply


class BoardListView(ListView):
    model = Board
    # template_name = "board/board_list.html"


class BoardDetailView(DetailView):
    model = Board
    # template_name = "board/board_detail.html"


class BoardCreateView(CreateView):
    model = Board
    # template_name = "board/board_form.html"
    fields = ['title', 'content']
