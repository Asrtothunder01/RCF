from rest_framework import serializers
from .models import Sermon, School

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'  # Include all fields of the Sermon model


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'  # Include all fields of the School model
