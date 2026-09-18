from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "date_joined",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (

        (
            "HireFlow Profile",
            {
                "fields": (
                    "role",
                    "bio",
                    "phone",
                    "profile_image",
                    "skills",
                )
            }
        ),
    )