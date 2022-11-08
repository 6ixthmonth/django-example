"""
모델 클래스를 작성하는 파일.

장고는 ORM(Object Relational Mapping) 방식으로 웹 애플리케이션과 데이터베이스를 연동하며, 이때 모델 클래스가 필요하다.
모델 클래스는 데이터베이스의 테이블을 나타내며, 클래스 변수는 테이블의 필드를, 모델 클래스로 만들어진 객체는 테이블의 레코드를 나타낸다.
모델을 알맞게 작성하고 데이터베이스 API 문법에 맞게 사용하면 자동으로 데이터베이스에 데이터를 조회하거나 입력하는 등의 조작을 할 수 있다.
"""


from django.contrib import admin

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """질문을 나타내는 모델."""

    question_text = models.CharField(max_length=200)  # 질문 텍스트.
    pub_date = models.DateTimeField('date published')  # 질문 작성일.

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     """최근 1일 이내 작성한 질문인지 검사하는 함수."""
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 관리자 페이지에서 이 항목을 어떻게 표시할지 설정하는 데코레이터.
    @admin.display(
        boolean=True,  # 논리형 데이터를 아이콘으로 표시할 지 여부를 설정.
        ordering='pub_date',  # 정렬 시 사용할 기준 필드.
        description='Published recently?',  # 이 항목에 대한 설명. 관리자 페이지에 표시한다.
    )
    def was_published_recently(self):
        """질문 작성일이 현재 시간보다 1일 전이면서 현재 시간 사이인지 검사하는 함수. 미래 시점으로 설정된 질문의 경우 False를 반환한다."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """선택지를 나타내는 모델. 외래 키로 질문을 가진다."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 이 선택지와 연결된 원본 질문.
    choice_text = models.CharField(max_length=200)  #  선택지 텍스트.
    votes = models.IntegerField(default=0)  # 투표 수.

    def __str__(self):
        return self.choice_text
