from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    ordering = ['date_joined']

admin.site.register(User, CustomUserAdmin)