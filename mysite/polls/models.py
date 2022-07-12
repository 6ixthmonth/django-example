import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """설문조사 앱에서 질문을 나타내는 모델."""
    question_text = models.CharField(max_length=200)  # 질문 텍스트.
    pub_date = models.DateTimeField('date published')  # 질문 작성일.

    def __str__(self):
        return self.question_text

    def was_published_recently(self) -> bool:
        """최근 1일 이내 작성한 질문인지 검사하는 함수."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """설문조사 앱에서 선택지를 나타내는 모델. 외래 키로 질문을 가진다."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 이 선택지와 연결된 원본 질문.
    choice_text = models.CharField(max_length=200)  #  선택지 텍스트.
    votes = models.IntegerField(default=0)  # 투표 수.

    def __str__(self):
        return self.choice_text
