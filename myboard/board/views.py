from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView


class board_list(ListView):
    model = None