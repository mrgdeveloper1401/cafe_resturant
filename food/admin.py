from django.contrib import admin
from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'category', 'food_number', 'sell_price', 'image', 'is_active', 'is_get_out', 'is_avaliable')
    search_fields = ('food_name', )
    list_filter = ('is_active', 'is_get_out', 'create_at', 'update_at')
    date_hierarchy = 'create_at'
    list_per_page = 20
    list_editable = ('is_active', 'is_get_out')
    prepopulated_fields = {'slug': ('food_name', )}
    raw_id_fields = ('category', 'pannel', 'image')


# @admin.register(FoodAttribute)
# class FoodAttributeAdmin(admin.ModelAdmin):
#     pass


# @admin.register(FoodAttributeValues)
# class FoodAttributeValuesAdmin(admin.ModelAdmin):
#     pass


