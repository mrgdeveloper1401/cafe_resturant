from django.contrib import admin
from .models import Food, FoodPrice


class FoodPriceInline(admin.TabularInline):
    model = FoodPrice
    extra = 0


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = (FoodPriceInline,)
    list_display = ('food_name', 'food_number', 'image', 'is_active', 'is_get_out')
    search_fields = ('food_name', )
    list_filter = ('is_active', 'is_get_out', 'create_at', 'update_at')
    date_hierarchy = 'create_at'
    list_per_page = 20
    list_editable = ('is_active', 'is_get_out')
    raw_id_fields = ('image',)


@admin.register(FoodPrice)
class FoodPriceAdmin(admin.ModelAdmin):
    list_display = ('buy_price','sell_price', 'discount', 'final_price')
    list_filter = ('discount', 'is_active', 'create_at', 'update_at')
    list_per_page = 20
    date_hierarchy = 'create_at'