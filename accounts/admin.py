from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import users, OtpCode, UserAddress

@admin.register(users)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("mobile_phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "create_at", "update_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile_phone", "password1", "password2"),
            },
        ),
    )
    list_display = ("mobile_phone", "email", "first_name", "last_name", "is_active", 'is_staff', 'is_superuser')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("mobile_phone", "first_name", "last_name", "email")
    ordering = ("mobile_phone",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ('create_at', 'update_at', 'last_login', 'is_active', 'is_staff', 'is_superuser')


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('mobile_phone', 'code', 'create_code')
    list_filter = ('create_code',)
    search_fields = ('mobile_phone', 'code')


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'address', 'postal_code','mobile_phone')
    list_filter = ('create_at', 'update_at')
    date_hierarchy = 'create_at'
    list_per_page = 30
    readonly_fields = ('create_at', 'update_at')
    raw_id_fields = ('user',)