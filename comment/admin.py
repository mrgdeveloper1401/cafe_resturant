from django.contrib import admin
from .models import Comment, Reply


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title_comment', 'food', 'user', 'is_active', 'rate_choose')
    search_fields = ('title_comment','food', 'user')
    list_filter = ('is_active', 'rate_choose', 'create_at', 'update_at')
    list_per_page = 20
    list_editable =('is_active',)


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_editable = ('is_active',)
    list_display = ('body', 'user', 'food', 'is_active')
    search_fields = ('body', 'user', 'food')
    list_per_page = 20
    