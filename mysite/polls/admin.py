"""
모델 관리자 클래스를 작성하는 파일.

이 파일을 통해서 특정 모델을 관리자 앱에 등록하기만 해도, 해당 모델과 연결된 데이터베이스 내 데이터를 관리자 페이지에서 조작할 수 있다.
모델 관리자 클래스를 작성해서 등록하면, 출력할 열 추가, 필터 기능, 검색 기능 등을 설정할 수 있다.
"""


from django.contrib import admin

from .models import Choice, Question


# 질문, 선택지 모델을 관리자 페이지에 등록한다.
# admin.site.register(Question)
# admin.site.register(Choice)


# class ChoiceInline(admin.StackedInline):
#     """질문 데이터를 생성할 때, 선택지 데이터 또한 함께 생성하기 위한 스택 형식의 사용자 정의 인라인 클래스."""

#     model = Choice  # 이 인라인 클래스로 다룰 모델 클래스를 지정.
#     extra = 3  # 하나의 질문에 기본적으로 세 개의 선택지를 만들 수 있도록 표시.


class ChoiceInline(admin.TabularInline):
    """질문 데이터를 생성할 때, 선택지 데이터 또한 함께 생성하기 위한 테이블 형식의 사용자 정의 인라인 클래스."""

    model = Choice  # 이 인라인 클래스로 다룰 모델 클래스를 지정.
    extra = 3  # 하나의 질문에 기본적으로 세 개의 선택지를 만들 수 있도록 표시.


class QuestionAdmin(admin.ModelAdmin):
    """질문 모델을 관리하기 위한 사용자 정의 모델 관리자 클래스."""

    # 질문 데이터를 생성 또는 수정할 때, 다룰 필드들을 간단하게 설정.
    # fields = ['pub_date', 'question_text']

    # 질문 데이터를 생성 또는 수정할 때, 다룰 필드들을 상세하게 설정.
    fieldsets = (
        (None, {  # 첫 번째 필드셋 이름.
            'fields': ('question_text',),  # 이 그룹에서 다룰 필드들.
        }),
        ('Date information', {  # 두 번째 필드셋 이름.
            'fields': ('pub_date',),  # 이 그룹에서 다룰 필드들.
            'classes': ('collapse',),  # 이 그룹을 기본적으로 숨김 처리.
            'description': 'The date of published.',  # 이 그룹에 대한 설명.
        }),
    )

    inlines = [ChoiceInline]  # 위에서 작성한 선택지 인라인 클래스를 등록.

    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 질문 목록에서 출력할 열 설정.
    list_filter = ['pub_date']  # 질문 목록에서 필터를 적용할 열 설정. 설정하면 지정된 열의 데이터를 빠르게 필터링 할 수 있도록 몇 가지 옵션을 제공해준다.
    search_fields = ['question_text']  # 문자열 필드에 대한 검색창을 추가. 여러 개의 필드를 추가하면 각각의 필드를 OR 조건으로 검색한다.


admin.site.register(Question, QuestionAdmin)  # 모델 클래스와 모델 관리자 클래스를 같이 등록.
