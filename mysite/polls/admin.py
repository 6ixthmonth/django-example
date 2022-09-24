from django.contrib import admin

from .models import Choice, Question


# admin.site.register(Question)  # 질문 모델을 관리자 페이지에 등록해서 직접 관리할 수 있게 만듦.
# admin.site.register(Choice)  # 관리자 페이지에 선택지 모델을 등록해서 일일이 관리하는 것보다 질문과 함께 관리하는 게 더 효율적이므로 주석 처리.


# class ChoiceInline(admin.StackedInline):
#     """질문 데이터를 생성할 때, 선택지 데이터 또한 함께 생성하기 위한 사용자 정의 인라인 클래스."""

#     model = Choice  # 이 인라인 클래스로 다룰 모델 클래스를 지정.
#     extra = 3  # 하나의 질문에 기본적으로 세 개의 선택지를 만들 수 있도록 표시.


class ChoiceInline(admin.TabularInline):
    """질문 데이터를 생성할 때, 선택지 데이터 또한 함께 생성하기 위한 사용자 정의 인라인 클래스."""

    model = Choice  # 이 인라인 클래스로 다룰 모델 클래스를 지정.
    extra = 3  # 하나의 질문에 기본적으로 세 개의 선택지를 만들 수 있도록 표시.


class QuestionAdmin(admin.ModelAdmin):
    """질문 모델을 관리하기 위한 사용자 정의 모델 관리자 클래스."""

    # 질문 데이터를 생성 또는 수정할 때, 다룰 필드들을 간단하게 설정.
    # fields = ['pub_date', 'question_text']

    # 질문 데이터를 생성 또는 수정할 때, 다룰 필드들을 상세하게 설정.
    fieldsets = (
        (None, {  # 첫 번째 필드 그룹 이름.
            'fields': ('question_text',),  # 해당 그룹에서 다룰 필드들.
        }),
        ('Date information', {  # 두 번째 필드 그룹 이름.
            'fields': ('pub_date',),  # 해당 그룹에서 다룰 필드들.
            'classes': ('collapse',),  # 이 그룹을 기본적으로 숨김 처리.
            'description': 'The date of published.',  # 이 그룹에 대한 설명.
        }),
    )

    inlines = [ChoiceInline]  # 위에서 작성한 인라인 클래스를 등록.

    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 질문 목록에서 표시할 열 설정.
    list_filter = ['pub_date']  # 질문 목록에서 필터를 적용할 열 설정. 설정하면 지정된 열의 데이터를 빠르게 필터링 하기 위해 몇 가지 옵션을 제공해준다.
    search_fields = ['question_text']  # 문자열 필드에 대한 검색창을 추가. 여러 개의 필드를 추가하면 각각의 필드를 OR 조건으로 검색한다.


admin.site.register(Question, QuestionAdmin)  # 모델 클래스와 모델 관리자 클래스를 같이 등록.
