from django.db import models
from django.utils import timezone

from textwrap import shorten

from user.models import User


class Board(models.Model):
    """게시글 클래스"""
    number = models.BigAutoField(primary_key=True)  # 게시글 번호
    title = models.CharField(max_length=40)  # 게시글 제목
    content = models.TextField(null=True, blank=True)  # 게시글 내용
    date = models.DateTimeField(default=timezone.now)  # 게시글 작성일
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 게시글 작성자

    def __str__(self) -> str:
        max_length:int = 0
        for key in vars(self).keys():
            max_length = len(key) if len(key) > max_length and not key.startswith("_") else max_length

        result = f"""{{
            {'number':{max_length}}: {self.number},
            {'title':{max_length}}: '{shorten(self.title, width=20, placeholder='...')}',
            {'content':{max_length}}: '{shorten(self.content, width=20, placeholder='...') if self.content != None else ''}',
            {'date':{max_length}}: {self.date:%Y-%m-%d %H:%M:%S},
            {'user':{max_length}}: {self.user},
        }}"""

        return result


class Reply(models.Model):
    """댓글 클래스"""
    content = models.TextField()  # 댓글 내용
    date = models.DateTimeField(default=timezone.now)  # 댓글 작성일
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 원본 게시글

    def __str__(self) -> str:
        max_length:int = 0
        for key in vars(self).keys():
            max_length = len(key) if len(key) > max_length and not key.startswith("_") else max_length

        result = f"""{{
            {'id':{max_length}}: {self.id},
            {'content':{max_length}}: '{shorten(self.content, width=20, placeholder='...')}',
            {'date':{max_length}}: {self.date:%Y-%m-%d %H:%M:%S},
            {'user':{max_length}}: {self.user},
            {'board_id':{max_length}}: {self.board_id}
        }}"""

        return result
