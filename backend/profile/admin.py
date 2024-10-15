from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin (admin.ModelAdmin):
    list_display = ['first_name',]
    search_fields = ['first_name','user_name']
    date_hierarchy = ['created_at']
    list_filter = ['user_name',]
    