from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from user.models import User
from .models import Board


def create_board(title='', content=None, date=timezone.now()):
    """테스트에 사용할 게시글을 생성하는 함수."""
    tester = User(id='tester', pw='1234', nm='테스터')
    tester.save()
    return Board.objects.create(title=title, content=content, date=date, user_id=tester.id)


class BoardListViewTests(TestCase):
    def test_not_exist_board(self):
        """게시글이 존재하지 않을 때 테스트."""
        response = self.client.get(reverse('board:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "게시글이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['board_list'], [])

    def test_exist_board(self):
        """게시글이 존재할 때 테스트."""
        board = create_board(title="게시글 테스트")
        response = self.client.get(reverse('board:list'))
        self.assertQuerysetEqual(
            response.context['board_list'],
            [board],
        )

    def test_two_boards(self):
        """게시글이 두 개 이상일 때 출력 순서 테스트."""
        board1 = create_board(title="게시글 테스트1", date=timezone.now()-timedelta(days=2))
        board2 = create_board(title="게시글 테스트2", date=timezone.now()-timedelta(days=1))
        response = self.client.get(reverse('board:list'))
        self.assertQuerysetEqual(
            response.context['board_list'],
            [board2, board1],
        )


class BoardDetailViewTests(TestCase):
    pass
