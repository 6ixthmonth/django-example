from django.contrib import admin

from .models import Board, Reply


class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('id', 'title', 'username', 'date')

    def username(self, obj):
        return obj.user.username


class ReplyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Board, BoardAdmin)
admin.site.register(Reply, ReplyAdmin)
