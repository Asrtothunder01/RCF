from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    preacher = models.CharField(max_length=100)
    theme = models.CharField(max_length=200)
    content = models.TextField()
    audio_file = models.FileField(upload_to='sermons/',null=True,blank=True)


class school(models.Model):
    title = models.CharField(max_length=200)

    date = models.DateField()

    topic = models.CharField(max_length= 200)

    memory_verse = models.CharField(max_length=300)
    content = models.TextField()
 