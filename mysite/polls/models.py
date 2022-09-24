from django.contrib import admin

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """설문조사 앱에서 질문을 나타내는 모델."""

    question_text = models.CharField(max_length=200)  # 질문 텍스트.
    pub_date = models.DateTimeField('date published')  # 질문 작성일.

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     """최근 1일 이내 작성한 질문인지 검사하는 함수."""
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 관리자 페이지에서 이 항목을 어떻게 표기할지 설정하는 데코레이터.
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """질문 작성일이 현재 시간보다 1일 전이면서 현재 시간 사이인지 검사하는 함수. 미래 시점으로 설정된 질문의 경우 False를 반환한다."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """설문조사 앱에서 선택지를 나타내는 모델. 외래 키로 질문을 가진다."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 이 선택지와 연결된 원본 질문.
    choice_text = models.CharField(max_length=200)  #  선택지 텍스트.
    votes = models.IntegerField(default=0)  # 투표 수.

    def __str__(self):
        return self.choice_text
