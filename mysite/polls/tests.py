"""
테스트 케이스 클래스를 작성하는 파일.

터미널에서 py manage.py test [앱 이름] 명령어를 실행하면 이곳에 작성된 테스트 케이스에 따라 자동화된 테스트(Automated test)를 실행한다.
테스트를 통해 모델에 대한 무결성 검사, 뷰의 정상 동작 확인 등을 할 수 있다.
"""


import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """작성일이 미래인 질문에 대해 was_published_recently() 함수가 False를 리턴하는지 검사한다."""
        time = timezone.now() + datetime.timedelta(days=30)  # 현재 시간으로부터 30일 이후의 시간 설정.
        future_question = Question(pub_date=time)  # 해당 시간(미래)의 질문 객체 생성.
        self.assertIs(future_question.was_published_recently(), False)  # 해당 질문 객체의 was_published_recently() 함수가 False를 반환하는지 검사.

    def test_was_published_recently_with_old_question(self):
        """작성일이 1일 이상 오래된 질문에 대해 was_published_recently() 함수가 False를 리턴하는지 검사한다."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)  # 현재 시간으로부터 1일 1초 전의 시간 설정.
        old_question = Question(pub_date=time)  # 해당 시간(과거)의 질문 객체 생성.
        self.assertIs(old_question.was_published_recently(), False)  # 해당 질문 객체의 was_published_recently() 함수가 False를 반환하는지 검사.

    def test_was_published_recently_with_recent_question(self):
        """작성일이 1일 이내인 질문에 대해 was_published_recently() 함수가 True를 리턴하는지 검사한다."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)  # 현재 시간으로부터 23시간 59분 59초 전의 시간 설정
        recent_question = Question(pub_date=time)  # 해당 시간(최근)의 질문 객체 생성.
        self.assertIs(recent_question.was_published_recently(), True)  # 해당 질문 객체의 was_published_recently() 함수가 True를 반환하는지 검사.


def create_question(question_text, days):
    """
    주어진 `question_text`로 질문을 생성하고 주어진 `days` 수를 현재 시간에 적용하여 게시한다
    (음수는 과거에 게시된 질문, 양수는 아직 게시하지 않은 질문).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """만약 질문이 존재하지 않으면, 적절한 메시지가 표시되는지 검사한다."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "등록된 설문이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """과거의 작성일을 가지는 질문이 index 페이지에 표시되는지 검사한다."""
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        """미래의 작성일을 가지는 질문이 index 페이지에 표시되지 않는지 검사한다."""
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "등록된 설문이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """만약 과거 및 미래 질문이 모두 존재하더라도 과거 질문만 표시되는지 검사한다."""
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_two_past_questions(self):
        """질문 index 페이지가 여러 개의 질문을 표시할 수 있는지 검사한다."""
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question2, question1])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """미래 작성일을 가지는 질문의 상세 뷰가 404 찾을 수 없음 오류를 반환하는지 검사한다."""
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """과거 작성일을 가지는 질문의 상세 뷰가 질문의 텍스트를 표시하는지 검사한다."""
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
