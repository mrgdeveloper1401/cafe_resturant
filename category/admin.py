from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'parent', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'create_at', 'update_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
    ordering= ('title',)
    date_hierarchy = 'update_at'