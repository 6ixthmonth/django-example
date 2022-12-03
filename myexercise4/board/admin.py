from django.contrib import admin

from .models import Board, Reply


admin.site.register((Board, Reply))
