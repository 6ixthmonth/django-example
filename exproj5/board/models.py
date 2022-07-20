from django.db import models
from django.utils import timezone

from textwrap import shorten

from user.models import User


class Board(models.Model):
    """게시글 모델을 표현하는 클래스."""

    number = models.BigAutoField(primary_key=True)  # 게시글 번호.
    title = models.CharField(max_length=40)  # 게시글 제목.
    content = models.TextField(null=True, blank=True)  # 게시글 내용.
    date = models.DateTimeField(default=timezone.now)  # 게시글 작성일.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 게시글 작성자.

    # 관리자 페이지에서 Board 객체 출력 시 사용.
    def __str__(self) -> str:
        return f"{shorten(self.title, width=20, placeholder='...')}"

    # 파이썬 셸에서 Board 객체 출력 시 사용.
    def __repr__(self) -> str:
        # 가장 긴 이름을 가진 속성의 글자 수를 구한다.
        max_attr_name_length = 0
        for attr_name in vars(self).keys():
            max_attr_name_length = len(attr_name) if len(attr_name) > max_attr_name_length and not attr_name.startswith("_") else max_attr_name_length

        return f"""{{
            {'number':{max_attr_name_length}}: {self.number},
            {'title':{max_attr_name_length}}: "{shorten(self.title, width=20, placeholder='...')}",
            {'content':{max_attr_name_length}}: "{shorten(self.content, width=20, placeholder='...') if self.content != None else ''}",
            {'date':{max_attr_name_length}}: {self.date:%Y-%m-%d %H:%M:%S},
            {'user_id':{max_attr_name_length}}: {self.user_id},
        }}"""

    def is_today_published(self) -> bool:
        """오늘 작성한 게시글 여부를 반환하는 함수."""
        board_date = self.date  # 게시글 작성일.
        today = timezone.now()  # 현재 시각.
        return (board_date.year == today.year) and (board_date.month == today.month) and (board_date.day == today.day)


class Reply(models.Model):
    """댓글 모델을 표현하는 클래스."""

    content = models.TextField()  # 댓글 내용.
    date = models.DateTimeField(default=timezone.now)  # 댓글 작성일.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자.
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 원본 게시글.

    # 관리자 페이지에서 Reply 객체 출력 시 사용.
    def __str__(self) -> str:
        return f"{shorten(self.content, width=20, placeholder='...')}"

    # 파이썬 셸에서 Reply 객체 출력 시 사용.
    def __repr__(self) -> str:
        # 가장 긴 이름을 가진 속성의 글자 수를 구한다.
        max_attr_name_length = 0
        for attr_name in vars(self).keys():
            max_attr_name_length = len(attr_name) if len(attr_name) > max_attr_name_length and not attr_name.startswith("_") else max_attr_name_length

        return f"""{{
            {'id':{max_attr_name_length}}: {self.id},
            {'content':{max_attr_name_length}}: "{shorten(self.content, width=20, placeholder='...')}",
            {'date':{max_attr_name_length}}: {self.date:%Y-%m-%d %H:%M:%S},
            {'user_id':{max_attr_name_length}}: {self.user_id},
            {'board_id':{max_attr_name_length}}: {self.board_id}
        }}"""
