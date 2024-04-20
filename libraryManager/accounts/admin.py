from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjUserAdmin

# Register your models here.


@admin.register(get_user_model())
class UserAdmin(DjUserAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "email",
        "first_name",
        "last_name",
        "mobile",
        "is_active",
    )

    search_fields = (
        "id",
        "mobile",
        "email",
    )

    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Basic Details",
            {
                "classes": ("wide", "extrapretty"),
                "fields": (
                    "first_name",
                    "last_name",
                    "mobile",
                ),
            },
        ),
        (
            "Roles/Permissions",
            {
                "classes": ("wide", "extrapretty"),
                "fields": (
                    ("is_active", "is_staff", "is_superuser"),
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
