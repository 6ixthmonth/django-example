from django.db import models
from django.utils import timezone

from textwrap import shorten

from user.models import User


class Board(models.Model):
    """게시글을 표현하는 모델 클래스."""

    number = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        attr_name_max_length = 0
        for attr_name in vars(self).keys():
            attr_name_max_length = len(attr_name) if not attr_name.startswith("_") and len(attr_name) > attr_name_max_length else attr_name_max_length
        return f"""{{
            {'number':{attr_name_max_length}}: {self.number},
            {'title':{attr_name_max_length}}: "{shorten(self.title, width=20, placeholder='...')}",
            {'content':{attr_name_max_length}}: "{shorten(self.content, width=20, placeholder='...') if self.content != None else ''}",
            {'date':{attr_name_max_length}}: {self.date:%Y-%m-%d %H:%M:%S},
            {'user_id':{attr_name_max_length}}: {self.user_id},
        }}"""

    def is_today_published(self) -> bool:
        """오늘 작성 여부를 반환하는 함수."""
        board_date = self.date
        today = timezone.now()
        return (board_date.year == today.year) and (board_date.month == today.month) and (board_date.day == today.day)


class Reply(models.Model):
    """댓글을 표현하는 모델 클래스."""

    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self) -> str:
        attr_name_max_length = 0
        for attr_name in vars(self).keys():
            attr_name_max_length = len(attr_name) if not attr_name.startswith("_") and len(attr_name) > attr_name_max_length else attr_name_max_length
        return f"""{{
            {'id':{attr_name_max_length}}: {self.id},
            {'content':{attr_name_max_length}}: "{shorten(self.content, width=20, placeholder='...')}",
            {'date':{attr_name_max_length}}: {self.date:%Y-%m-%d %H:%M:%S},
            {'user_id':{attr_name_max_length}}: {self.user_id},
            {'board_id':{attr_name_max_length}}: {self.board_id}
        }}"""
