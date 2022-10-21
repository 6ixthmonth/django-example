from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from textwrap import shorten


class Board(models.Model):
    """게시글 모델 클래스."""

    title = models.CharField(max_length=40, verbose_name='제목')  # 제목.
    content = models.TextField(verbose_name='내용', default='')  # 내용.
    date = models.DateTimeField(default=timezone.now)  # 작성일.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 작성자. User 모델을 FK로 설정.
    attached_file = models.FileField(upload_to='board/%Y-%m-%d/', null=True)  # 첨부 파일.
    original_filename = models.CharField(max_length=260, null=True)  # 파일 이름.

    def __str__(self) -> str:
        return shorten(self.title, width=20, placeholder='...')


class Reply(models.Model):
    """댓글 모델 클래스."""

    content = models.TextField()  # 내용.
    date = models.DateTimeField(default=timezone.now)  # 작성일.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 작성자.
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 원본 게시글.

    def __str__(self) -> str:
        return shorten(self.content, width=20, placeholder='...')
