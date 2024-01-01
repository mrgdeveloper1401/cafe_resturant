from django.contrib import admin
from .models import Pannel, Sciol, SciolValues
from food.models import Food, FoodPrice


class FoodInline(admin.TabularInline):
    model = Food
    extra = 0


class SciolValueInline(admin.TabularInline):
    model = SciolValues
    extra = 0


class FoodPriceInline(admin.TabularInline):
    model = FoodPrice
    extra = 0


@admin.register(Pannel)
class PannelAdmin(admin.ModelAdmin):
    inlines = (FoodInline, FoodPriceInline, SciolValueInline)
    raw_id_fields = ('user',)
    list_filter = ('is_active', 'create_at', 'update_at')
    list_display = ('user', 'pannel_name', 'is_active', 'create_at', 'update_at')
    list_editable = ('is_active',)
    search_fields = ('pannel_name', )
    list_per_page = 20
    date_hierarchy = 'create_at'


@admin.register(Sciol)
class SciolAdmin(admin.ModelAdmin):
    inlines = (SciolValueInline,)


@admin.register(SciolValues)
class SciolValuesAdmin(admin.ModelAdmin):
    pass


