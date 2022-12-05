from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserProfileAdmin(auth_admin.UserAdmin):
    list_display = (
        'username',
        'date_of_birth',
        'email', 'phone',
        'profession', 'photo'
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", 'date_of_birth', 'email',
                                      "phone", 'profession', 'photo')}),
        ("Permissions",
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
        (("Important dates",), {"fields": ("last_login", "date_joined")}),
    )
