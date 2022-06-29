from django.db import models
from django.utils import timezone

from user.models import User


class Board(models.Model):
    """게시글 클래스"""
    board_num = models.BigAutoField(primary_key=True)  # 게시글 번호
    board_title = models.CharField(max_length=50)  # 게시글 제목
    board_content = models.TextField()  # 게시글 내용
    board_date = models.DateTimeField(default=timezone.now)  # 게시글 작성일
    board_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 게시글 작성자

    def __str__(self) -> str:
        result = f"""
        {{
            board_num: {self.board_num},
            board_title: {self.board_title},
            board_date: {self.board_date},
            board_user: {self.board_user}
        }}
        """

        return result


class Reply(models.Model):
    """댓글 클래스"""
    reply_content = models.TextField()  # 댓글 내용
    reply_date = models.DateTimeField(default=timezone.now)  # 댓글 작성일
    reply_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    reply_board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 원본 게시글

    def __str__(self) -> str:
        result = f"""
        {{
            id: {self.id},
            reply_date: {self.reply_date},
            reply_user: {self.reply_user},
            reply_board.board_num: {self.reply_board.board_num}
        }}
        """

        return result
