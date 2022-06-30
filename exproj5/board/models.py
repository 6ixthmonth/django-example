from django.db import models
from django.utils import timezone

from textwrap import shorten

from user.models import User


class Board(models.Model):
    """게시글 클래스"""
    board_num = models.BigAutoField(primary_key=True)  # 게시글 번호
    board_title = models.CharField(max_length=50)  # 게시글 제목
    board_content = models.TextField(null=True, default='')  # 게시글 내용
    board_date = models.DateTimeField(default=timezone.now)  # 게시글 작성일
    board_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 게시글 작성자

    def __str__(self) -> str:
        max_length:int = 0
        for key in vars(self).keys():
            max_length = len(key) if len(key) > max_length and not key.startswith("_") else max_length

        result = f"""{{
            {'board_num':{max_length+1}}: {self.board_num},
            {'board_title':{max_length+1}}: '{self.board_title}',
            {'board_content':{max_length+1}}: '{shorten(self.board_content, width=20, placeholder='...')}',
            {'board_date':{max_length+1}}: {self.board_date: %Y-%m-%d %H:%M:%S},
            {'board_user':{max_length+1}}: {self.board_user},
        }}"""

        return result


class Reply(models.Model):
    """댓글 클래스"""
    reply_content = models.TextField()  # 댓글 내용
    reply_date = models.DateTimeField(default=timezone.now)  # 댓글 작성일
    reply_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    reply_board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 원본 게시글

    def __str__(self) -> str:
        max_length:int = 0
        for key in vars(self).keys():
            max_length = len(key) if len(key) > max_length and not key.startswith("_") else max_length

        result = f"""{{
            {'id':{max_length+1}}: {self.id},
            {'reply_content':{max_length+1}}: '{shorten(self.reply_content, width=20, placeholder='...')}',
            {'reply_date':{max_length+1}}: {self.reply_date: %Y-%m-%d %H:%M:%S},
            {'reply_user':{max_length+1}}: {self.reply_user},
            {'reply_board_id':{max_length+1}}: {self.reply_board_id}
        }}"""

        return result
