from rest_framework import serializers

from .models import Dashboard, Widget, User

from rest_framework.exceptions import APIException


# Serializers


'''UserSerializers'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = User
        
        fields = ['id','first_name','last_name','email','username','date_joined']
        
        read_only_fields = ['id','date_joined']
  
              
#Dashboard Serializer


''' DashboardSerializer'''

class DashboardSerializer(serializers.ModelSerializer):
    
    # Nested Serializers For better representation  
    user = UserSerializer (read_only = True)
    
    class Meta:
        model = Dashboard
        
        fields = ['id','user','name','description','created_at']
        
        def validate_name(self, value):
            if not value:
                raise Serializers.ValidationError(' Name is required')
            return value
        


# WidgetSerializer


'''WidgetSerializer'''


class WidgetSerializer(serializers.ModelSerializers):
    
# Nested Serializers

    dashboard = DashboardSerializer(read_only = True)
    
    #validate foreign Key fields
    def validate_dashboard(self, value):
        if value is None:
            raise serializers.ValidationError('dashboard is required')
        if not Dashboard.objects.filter(id=('link  unavailable')).exists():
            raise serializers.ValidationError('Dashboard does not exists')
        return value
        
                        
#add serializerMethodField to audio_url_field

    audio_file_url = serializers.SerializerMethodField()
    
    # Handle exception
    
    def get_audio_file_url(self,obj):
        try:
            return obj.audio_file_url
        except AttributeError:
            raise APIException ('Audio File Not Found')
        except Exception as e:
            raise APIEXCEPTION('Error Retrieving Audio file Url')
        
    class Meta:
        model = Widget
        fields = ['id','dashboard','audio_file','audio_type','album_art','type','created_at','updated_at']
        

  