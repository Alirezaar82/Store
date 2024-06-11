from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile,UserAddressModel
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for user management with add and change forms plus password
    """

    model = User
    list_display = ("id","phone_number", "is_superuser", "is_active", "is_verified")
    list_filter = ("phone_number", "is_superuser", "is_active", "is_verified")
    searching_fields = ("phone_number",)
    ordering = ("phone_number",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("phone_number", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions","type"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "type"
                ),
            },
        ),
    )


@admin.register(Profile)
class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ("id","user", "first_name","last_name",'email')
    searching_fields = ("user","first_name","last_name",'email')



# from django.contrib.sessions.models import Session
# class SessionAdmin(admin.ModelAdmin):
#     def _session_data(self, obj):
#         return obj.get_decoded()
#     list_display = ['session_key', '_session_data', 'expire_date']
#     readonly_fields = ['_session_data']
# admin.site.register(Session, SessionAdmin)

@admin.register(UserAddressModel)
class UserAddressModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "state",
        "city",
        "zip_code",
        "created_date"
    )
