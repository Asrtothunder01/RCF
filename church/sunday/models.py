from django.db import models

class SundaySchoolLesson(models.Model):
    title = models.CharField(max_length=200)  # e.g., "Faith in Action"
    topic = models.CharField(max_length=200)  # e.g., "Walking by Faith"
    date = models.DateField()  # e.g., 2024-12-29
    memory_verse = models.TextField()  # e.g., "Now faith is the substance..."
    banner_image = models.ImageField(upload_to='lesson_banners/', null=True, blank=True)  # Optional banner image

    def __str__(self):
        return self.title

class LessonSection(models.Model):
    lesson = models.ForeignKey(SundaySchoolLesson, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=100)  # e.g., "Introduction"
    content = models.TextField()  # Section content

    def __str__(self):
        return f"{self.lesson.title} - {self.title}"

class ReflectionQuestion(models.Model):
    lesson = models.ForeignKey(SundaySchoolLesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()  # e.g., "What does it mean to walk by faith?"

    def __str__(self):
        return f"Question for {self.lesson.title}"

class FurtherReading(models.Model):
    lesson = models.ForeignKey(SundaySchoolLesson, on_delete=models.CASCADE, related_name='further_readings')
    title = models.CharField(max_length=200)  # e.g., "Hebrews 11:1-40"
    url = models.URLField(null=True, blank=True)  # Optional: Link to the reference

    def __str__(self):
        return f"{self.title} ({self.lesson.title})"