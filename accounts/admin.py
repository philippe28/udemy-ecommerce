from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'name', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        (
        'Informassões Básicas',{
        'fields':('name','last_login')
        }),
        (
            'permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'name', 'email',
                    'is_active', 'is_staff', 'data_joined']


admin.site.register(User, UserAdmin)

# Register your models here.
