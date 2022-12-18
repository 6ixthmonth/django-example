from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from user.tests import create_user
from .models import Board, Reply


def create_board(title="검사 게시글", content=None, date=timezone.now(), user_id="tester") -> Board:
    """검사에 사용할 게시글을 생성하는 함수."""
    return Board.objects.create(title=title, content=content, date=date, user_id=user_id)


def create_reply(content="", date=timezone.now(), user_id="tester", board_id=1) -> Reply:
    """검사에 사용할 댓글을 생성하는 함수."""
    return Reply.objects.create(content=content, date=date, user_id=user_id, board_id=board_id)


class BoardModelTests(TestCase):
    """게시글 모델을 검사하는 클래스."""

    def test_is_today_published_with_today_board(self):
        """오늘 작성한 게시글에 대해, is_today_published() 함수가 True를 반환하는지 검사하는 함수."""
        user = create_user()  # 게시글 작성자 생성.
        board = create_board(date=timezone.now(), user_id=user.id)  # 오늘 작성한 게시글 생성.
        self.assertEqual(board.is_today_published(), True)  # 함수 반환값 검증.

    def test_is_today_published_with_past_board(self):
        """과거 작성한 게시글에 대해, is_today_published() 함수가 False를 반환하는지 검사하는 함수."""
        user = create_user()  # 게시글 작성자 생성.
        board = create_board(date=timezone.now()-timedelta(days=1), user_id=user.id)  # 1일 전 작성한 게시글 생성.
        self.assertEqual(board.is_today_published(), False)  # 함수 반환값 검증.


class BoardListViewTests(TestCase):
    """게시글 목록 뷰를 검사하는 클래스."""

    def test_board_not_exists(self):
        """게시글이 존재하지 않을 때, 게시글 목록 페이지의 출력을 테스트한다."""
        response = self.client.get(reverse('board:list'))  # 게시글 목록 페이지 접속.

        self.assertEqual(response.status_code, 200)  # HTTP 상태 코드 검증.
        self.assertContains(response, "게시글이 존재하지 않습니다.")  # 페이지 본문 검증.
        self.assertQuerysetEqual(response.context['board_list'], [])  # 콘텍스트 검증.

    def test_board_is_exists(self):
        """게시글이 존재할 때, 게시글 목록 페이지의 출력을 테스트한다."""
        user = create_user()  # 게시글 작성자 생성.
        board = create_board(title="게시글 테스트", user_id=user.id)  # 게시글 생성.
        response = self.client.get(reverse('board:list'))  # 게시글 목록 페이지 접속.

        self.assertQuerysetEqual(response.context['board_list'], [board])  # 콘텍스트 검증.

    def test_two_boards(self):
        """게시글이 두 개 존재할 때, 게시글들의 출력 순서를 테스트한다."""
        user = create_user()  # 게시글 작성자 생성.
        board1 = create_board(title="게시글 테스트1", date=timezone.now()-timedelta(days=2), user_id=user.id)  # 2일 전 게시글 생성.
        board2 = create_board(title="게시글 테스트2", date=timezone.now()-timedelta(days=1), user_id=user.id)  # 1일 전 게시글 생성.
        response = self.client.get(reverse('board:list'))  # 게시글 목록 페이지 접속.

        self.assertQuerysetEqual(response.context['board_list'], [board2, board1])  # 콘텍스트 검증.


class BoardDetailViewTests(TestCase):
    """게시글 상세 뷰를 검사하는 클래스."""

    def test_reply_not_exists(self):
        """댓글이 존재하지 않을 때, 게시글 상세 페이지의 출력을 테스트한다."""
        user = create_user()  # 게시글 작성자 생성.
        board = create_board(user_id=user.id)  # 게시글 생성.
        response = self.client.get(reverse('board:detail', args=(board.number,)))  # 게시글 상세 페이지 접속.

        self.assertQuerysetEqual(response.context['board'].reply_set.all(), [])  # 콘텍스트 검증.

    def test_reply_is_exists(self):
        """댓글이 존재할 때, 게시글 상세 페이지의 출력을 테스트한다."""
        user = create_user()  # 게시글 및 댓글 작성자 생성.
        board = create_board(user_id=user.id)  # 게시글 생성.
        reply = create_reply(content="댓글 테스트", user_id=user.id, board_id=board.number)  # 댓글 생성.
        response = self.client.get(reverse('board:detail', args=(board.number,)))  # 게시글 상세 페이지 접속.

        self.assertQuerysetEqual(response.context['board'].reply_set.all(), [reply])  # 콘텍스트 검증.

    def test_two_replys(self):
        """댓글이 두 개 존재할 때, 댓글들의 출력 순서를 테스트한다."""
        user = create_user()  # 게시글 및 댓글 작성자 생성.
        board = create_board(user_id=user.id)  # 게시글 생성.
        reply1 = create_reply(content="댓글 테스트1", user_id=user.id, board_id=board.number)  # 댓글 생성.
        reply2 = create_reply(content="댓글 테스트2", user_id=user.id, board_id=board.number)  # 댓글 생성.
        response = self.client.get(reverse('board:detail', args=(board.number,)))  # 게시글 상세 페이지 접속.

        self.assertQuerysetEqual(list(response.context['board'].reply_set.all()), [reply1, reply2])  # 콘텍스트 검증.
