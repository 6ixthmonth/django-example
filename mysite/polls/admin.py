from django.contrib import admin

from .models import Question


admin.site.register(Question)  # 질문 모델을 관리자 페이지에 등록해서 직접 관리할 수 있게 만듦.
