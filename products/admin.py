from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'product_number', 'sell_price', 'image', 'is_active', 'is_get_out', 'is_avaliable')
    search_fields = ('product_name', )
    list_filter = ('is_active', 'is_get_out', 'create_at', 'update_at')
    date_hierarchy = 'create_at'
    list_per_page = 20
    list_editable = ('is_active', 'is_get_out')
    prepopulated_fields = {'slug': ('product_name', )}
    raw_id_fields = ('category', 'image')


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
