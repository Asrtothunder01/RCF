from django.contrib import admin
from .models import Sermon

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    """
    Admin interface for Sermon.
    """
    list_display = ('title', 'memory_verse')  # Columns displayed in the admin list view
    search_fields = ('title', 'memory_verse')  # Fields to search in the admin panel
    list_filter = ('title',)  # Add filtering by title
    fields = (
        'title',
        'memory_verse',
        'note',
        'further_reading',
        'audio_file',
        'banner_image',
    )  # Fields displayed in the form view
    readonly_fields = ()  # Specify any fields that should be read-only in the admin panel
