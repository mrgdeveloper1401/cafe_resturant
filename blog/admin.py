from django.contrib import admin
from .models import Post, Comment, Authore


@admin.register(Authore)
class AuthoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    list_display = ('title', 'author', 'is_active', 'id')
    list_per_page = 20
    list_editable = ('is_active',)
    search_fields = ('title', 'author', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

