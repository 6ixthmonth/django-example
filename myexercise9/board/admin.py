from django.contrib import admin
from django.utils.html import format_html

from .models import Board, Reply


class ReplyInline(admin.TabularInline):
    """게시글 모델 데이터 조작 시 댓글 모델 데이터 또한 함께 처리하기 위한 인라인 클래스."""

    model = Reply  # 인라인으로 처리할 모델 클래스.
    extra = 1  # 기본 개수.


class BoardAdmin(admin.ModelAdmin):
    """게시글 모델 데이터를 조작하기 위한 모델 관리자 클래스."""

    # 관리자 페이지에서 다룰 필드 그룹들.
    fieldsets = (
        ('Required Fields', {
            'fields': (
                'title', 'user',
            ),
        }),
        ('Optional Fields', {
            'fields': (
                'content',
            ),
        }),
        ('Auto-generated Fields', {
            'fields': (
                'date',
            ),
        }),
    )

    inlines = (ReplyInline,)  # 게시글 모델 데이터를 조작할 때 댓글 모델 데이터 또한 함께 조작함.

    list_display = ('number', 'board_title', 'date', 'user_nm')  # 게시글 목록에서 표시할 열의 목록.

    def board_title(self, obj):
        """board_title 필드를 정의하는 함수."""
        url = f"{obj.number}/change/"
        title = obj.title
        return format_html("<a href='{url}'>{title}</a>", url=url, title=title)

    def user_nm(self, obj):
        """user_nm 필드를 정의하는 함수."""
        return obj.user.nm

    def get_readonly_fields(self, request, obj=None):
        if obj:  # obj -> 데이터를 수정할 객체. 데이터를 생성할 땐 None으로 초기화됨.
            return self.readonly_fields + ('user', 'date',)  # 데이터를 수정할 때 user, date 필드를 readonly로 처리.
        return self.readonly_fields


admin.site.register(Board, BoardAdmin)
