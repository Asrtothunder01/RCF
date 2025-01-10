from django.contrib import admin
from .models import SundaySchoolLesson, LessonSection, ReflectionQuestion, FurtherReading

class LessonSectionInline(admin.StackedInline):
    """
    Inline admin interface for LessonSection.
    Allows adding/editing sections directly within a SundaySchoolLesson.
    """
    model = LessonSection
    extra = 1  # Number of empty forms to display
    fields = ['title', 'content']


class ReflectionQuestionInline(admin.TabularInline):
    """
    Inline admin interface for ReflectionQuestion.
    Allows adding/editing reflection questions within a SundaySchoolLesson.
    """
    model = ReflectionQuestion
    extra = 1  # Number of empty forms to display
    fields = ['question_text']


class FurtherReadingInline(admin.TabularInline):
    """
    Inline admin interface for FurtherReading.
    Allows adding/editing further readings within a SundaySchoolLesson.
    """
    model = FurtherReading
    extra = 1  # Number of empty forms to display
    fields = ['title', 'url']


@admin.register(SundaySchoolLesson)
class SundaySchoolLessonAdmin(admin.ModelAdmin):
    """
    Admin interface for SundaySchoolLesson.
    """
    list_display = ('title', 'topic', 'date')  # Columns displayed in the admin list view
    search_fields = ('title', 'topic')  # Fields to search in the admin panel
    list_filter = ('date',)  # Add filtering by date
    inlines = [LessonSectionInline, ReflectionQuestionInline, FurtherReadingInline]  # Inline related models
    prepopulated_fields = {'topic': ('title',)}  # Auto-fill topic based on the title


@admin.register(LessonSection)
class LessonSectionAdmin(admin.ModelAdmin):
    """
    Admin interface for LessonSection.
    """
    list_display = ('lesson', 'title')  # Columns displayed in the admin list view
    search_fields = ('lesson__title', 'title')  # Fields to search in the admin panel


@admin.register(ReflectionQuestion)
class ReflectionQuestionAdmin(admin.ModelAdmin):
    """
    Admin interface for ReflectionQuestion.
    """
    list_display = ('lesson', 'question_text')  # Columns displayed in the admin list view
    search_fields = ('lesson__title', 'question_text')  # Fields to search in the admin panel


@admin.register(FurtherReading)
class FurtherReadingAdmin(admin.ModelAdmin):
    """
    Admin interface for FurtherReading.
    """
    list_display = ('lesson', 'title', 'url')  # Columns displayed in the admin list view
    search_fields = ('lesson__title', 'title', 'url')  # Fields to search in the admin panel
