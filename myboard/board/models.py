from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from textwrap import shorten


class Board(models.Model):
    """게시글 모델 클래스."""

    number = models.BigAutoField(primary_key=True)  # 게시글 번호. 기본 키로 설정.
    title = models.CharField(max_length=40, verbose_name='제목')  # 게시글 제목.
    content = models.TextField(verbose_name='내용')  # 게시글 내용.
    date = models.DateTimeField(default=timezone.now)  # 게시글 작성일.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 게시글 작성자.
    attached_file = models.FileField(upload_to='board/%Y-%m-%d/', null=True)  # 첨부 파일. upload_to 폴더에 저장한다.
    original_file_name = models.CharField(max_length=260, null=True)  # 원본 파일 이름.

    def __str__(self) -> str:
        return shorten(self.title, width=20, placeholder='...')


class Reply(models.Model):
    """댓글 모델 클래스."""

    content = models.TextField()  # 댓글 내용.
    date = models.DateTimeField(default=timezone.now)  # 댓글 작성일.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자.
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 원본 게시글.

    def __str__(self) -> str:
        return shorten(self.content, width=20, placeholder='...')
