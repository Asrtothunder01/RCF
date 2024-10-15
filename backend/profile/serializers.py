from rest_framework import serializers
from .models import Profile

class ProfileSerializer (serializers.ModelSerializers):
    class Meta:
        models = Profile
        fields = ['id','user_name','first_name','last_name','address','created_at']
        
        read_only_fields = ['id','created_at']
    