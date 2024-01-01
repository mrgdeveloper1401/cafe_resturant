from django.contrib import admin
from .models import Contact, ContactUs


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email','mobile_phone', 'description', 'location')
    search_fields = ('email','mobile_phone', )
    list_filter = ('create_at', 'update_at')
    list_per_page = 20
    date_hierarchy = 'create_at'