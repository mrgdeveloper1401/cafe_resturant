from django.contrib import admin
from .models import WaysofCommunication, ContactUs


@admin.register(WaysofCommunication)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_phone', 'email', 'be_answered')
    list_filter = ('create_at', 'update_at')
    list_per_page = 20
    search_fields = ('first_name', 'last_name','mobile_phone', 'email', 'body')