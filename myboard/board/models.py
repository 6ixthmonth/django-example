from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from textwrap import shorten


class Board(models.Model):
    number = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=40, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return shorten(self.title, width=20, placeholder='...')


class Reply(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
