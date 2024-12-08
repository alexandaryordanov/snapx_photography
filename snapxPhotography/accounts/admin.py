from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from snapxPhotography.accounts.forms import MyAppUserCreationForm, MyAppUserChangeForm

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = MyAppUserCreationForm
    form = MyAppUserChangeForm

    list_display = ('pk', 'username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )