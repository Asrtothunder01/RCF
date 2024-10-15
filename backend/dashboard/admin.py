from django.contrib import admin

from .models import User, Dashboard, Widget

#Register your models here.

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'first_name','last_name')
    
    search_fields = ('username','email')
    

@admin.register(Dashboard)

class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name','user','created_at')
    
    search_fields = ('name','user__username')

        
@admin.register(Widget)

class WidgetAdmin(admin.ModelAdmin):
    list_display = ('type','dashboard',' created_at')
    
    search_fields = ('type','dashboard__type')