from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class UserCreationForm2(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username",)


@admin.register(UserModel)
class UserProfileAdmin(auth_admin.UserAdmin):
    form = UserCreationForm2
    add_form = UserCreationForm2
    list_display = (
        'username',
        'date_of_birth',
        'email', 'phone',
        'profession', 'photo'
    )

    fieldsets = (
        (None, {"fields": ("username", "password", )}),
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
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name", "date_of_birth", 'email',
                                      "phone", 'profession', 'photo'),
            },
        ),
    )




