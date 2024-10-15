import uuid
from django.db import models

class  Profile (models.Model):
    
    id = models.UUIDField(unique = True, primary_key = True, editable = False, default = uuid.uuid4)
    
    first_name = models.CharField(max_length = 50,help_text = 'Your Firstname', blank = True)
    
    last_name = models.CharField(max_length = 30,help_text = 'Your Lastname', blank = True,null = True)
    
    user_name = models.CharField(max_length = 50,help_text = 'Your Nickname', blank = True, unique= True,null = True)
    
    address = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name
        
       