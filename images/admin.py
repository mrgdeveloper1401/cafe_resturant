from django.contrib import admin
from .models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image_hash', 'image_size', 'alter_image', 'width', 'height', 'is_active')
    list_filter = ('create_at', 'update_at')
    list_editable = ('is_active',)
    list_per_page = 20
    date_hierarchy = 'create_at'
