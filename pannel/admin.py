from django.contrib import admin
from .models import Pannel, Sciol, SciolValues


class SciolValueInline(admin.TabularInline):
    model = SciolValues
    extra = 0


@admin.register(Pannel)
class PannelAdmin(admin.ModelAdmin):
    pass


@admin.register(Sciol)
class SciolAdmin(admin.ModelAdmin):
    inlines = (SciolValueInline,)


@admin.register(SciolValues)
class SciolValuesAdmin(admin.ModelAdmin):
    pass


