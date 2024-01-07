from django.contrib import admin
from .models import Product, Category, ProductAtrribute, ProductAttributeValue, Brand
from django.utils.translation import gettext_lazy as _


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductAttributeValueInline,)
    fieldsets = [
        (
            'دسته بندی',
            {
                'fields': ('category', 'type_category', 'brand'),
            }
        ),
        (
            'محصول',
            {
                'fields': ('en_product_name', 'product_name', 'slug', 'image', 'description'),
            }
        ),
        (
            'قیمت محصول',
            {
                'fields': ('buy_price','sell_price', 'discount',),
            }
        ),
        (
            'دسترسی ها',
            {
                'fields': ('is_active', 'is_get_out', 'is_avaliable'),
            }
        )
    ]
    list_display = ('en_product_name', 'product_name', 'type_category', 'product_number', 'sell_price', 'image', 'is_active', 'is_get_out', 'is_avaliable')
    search_fields = ('product_name', )
    list_filter = ('is_active', 'is_get_out', 'create_at', 'update_at', 'category', 'type_category')
    date_hierarchy = 'create_at'
    list_per_page = 20
    list_editable = ('is_active', 'is_get_out')
    prepopulated_fields = {'slug': ('en_product_name', )}
    raw_id_fields = ('image',)
    filter_horizontal = ('category',)
    list_display_links = ('en_product_name', 'product_name')


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


@admin.register(ProductAtrribute)
class ProductAtrributeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand_name',)}
    list_display = ('brand_name','slug', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'create_at', 'update_at', 'brand_name')
    list_per_page = 20
    