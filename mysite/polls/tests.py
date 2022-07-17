import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        질문 작성일이 미래인 경우 was_published_recently() 함수가 False를 리턴하는지 검사한다.
        """
        time = timezone.now() + datetime.timedelta(days=30)  # 현재 시점으로부터 30일 이후의 날짜시간 설정.
        future_question = Question(pub_date=time)  # 해당 시간의 질문 객체 생성.
        self.assertIs(future_question.was_published_recently(), False)  # 해당 질문 객체에서 was_published_recently() 함수를 실행하면 False가 반환되는지 검사.

    def test_was_published_recently_with_old_question(self):
        """
        질문 작성일이 1일 이상 오래된 경우 was_published_recently() 함수가 False를 리턴하는지 검사한다.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        질문 작성일이 1일 이내인 경우 was_published_recently() 함수가 True를 리턴하는지 검사한다.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    주어진 `question_text`로 질문을 생성하고 주어진 `days` 수를 현재로부터 적용하여 게시한다
    (음수의 경우 과거, 양수의 경우 아직 게시하지 않은 질문).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        만약 질문이 존재하지 않으면, 적절한 메시지가 출력된다.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "등록된 설문이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        과거의 게시일을 가지는 질문이 index 페이지에 출력된다.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        미래의 게시일을 가지는 질문이 index 페이지에 출력되지 않는다.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "등록된 설문이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        만약 과거 및 미래 질문 양쪽 모두 존재한다면, 과거 질문만 출력된다.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        """
        질문 index 페이지가 여러 개의 질문을 출력할 것이다.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
