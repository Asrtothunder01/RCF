from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sermon Title")
    date = models.DateField(verbose_name="Date of Sermon")
    preacher = models.CharField(max_length=100, verbose_name="Preacher's Name")
    theme = models.CharField(max_length=200, verbose_name="Sermon Theme", null=True, blank=True)
    content = models.TextField(verbose_name="Sermon Content")
    audio_file = models.FileField(upload_to='sermons/', null=True, blank=True, verbose_name="Audio File")

    class Meta:
        verbose_name = "Sermon"
        verbose_name_plural = "Sermons"
        ordering = ['-date']  # Orders by most recent first

    def __str__(self):
        return self.title


class School(models.Model):  # Renamed to follow PascalCase convention
    title = models.CharField(max_length=200, verbose_name="Lesson Title")
    date = models.DateField(verbose_name="Date of Lesson")
    topic = models.CharField(max_length=200, verbose_name="Lesson Topic")
    memory_verse = models.CharField(max_length=300, verbose_name="Memory Verse")
    content = models.TextField(verbose_name="Lesson Content")

    class Meta:
        verbose_name = "School Lesson"
        verbose_name_plural = "School Lessons"
        ordering = ['-date']  # Orders by most recent first

    def __str__(self):
        return self.title
