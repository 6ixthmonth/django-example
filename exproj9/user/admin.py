from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """desc"""

    fields = ('id', 'pw', 'nm',)  # 관리자 페이지에서 이 모델에 대해 다룰 필드들.

    def get_readonly_fields(self, request, obj=None):
        if obj:  # obj -> 데이터를 수정할 객체. 데이터를 생성할 땐 None으로 초기화됨.
            return self.readonly_fields + ('id',)  # 데이터를 수정할 때 id 필드를 readonly로 처리.
        return self.readonly_fields


admin.site.register(User, UserAdmin)
