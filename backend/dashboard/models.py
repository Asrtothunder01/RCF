from django.db import models

import uuid

# User Models

class User(models.Model):
    id = models.UUIDField(unique = True, editable = False, primary_key = True, default = uuid.uuid4)
    
    user_name = models.CharField(max_length = 20, blank =True, unique = True)
    
    email = models.EmailField(unique = True)
    
    first_name = models.CharField(max_length = 50)
    
    last_name = models.CharField(max_length = 50)
    
    date_joined = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name
    
    
#Dashboard Models 

class Dashboard (models.Model):
    
    id = models.UUIDField(unique = True, editable = False, primary_key = True, default = uuid.uuid4)
    
    name = models.CharField(max_length = 50)
    
    description = models.TextField()
    
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    
    created_at = models.DateTimeField(auto_now_add = True)
 
   def __str__(self):
       return f"{self.name}-{self.user}"
       
 
 
 # Audio

AUDIO_TYPES = [
       ('mp3','MP3'),
       ('wav','WAV'),
       ('ogg','OGG'),
    ]
    

    
            
# widget Models

class Widget (models.Model):
    
    id = models.UUIDField(unique = True, editable = False, primary_key = True, default = uuid.uuid4)
    
    dashboard = models.ForeignKey(Dashboard,on_delete = models.CASCADE,null = True)
    
    audio_file = models.FileField(upload_to = 'audio_files/',null = True)
    
    audio_type = models.CharField(max_length = 50,choices = AUDIO_TYPES,null = True)
    
    album_art = models.ImageField(upload_to = 'album_art/',null = True)
    
    type = models.CharField(max_length = 50)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at =models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.dashboard.name}-{self.type}"
        