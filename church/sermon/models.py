from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    memory_verse = models.CharField(max_length=255)
    note = models.TextField()
    further_reading = models.TextField(blank=True, null=True)
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    banner_image = models.ImageField(upload_to='sermons/images/', blank=True, null=True)

    def __str__(self):
        return self.title
