from rest_framework.generics import  ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated
from .models import User, Dashboard,Widget

from .Serializers import WidgetSerializer, DashboardSerializer, UserSerializer

from rest_framework.exceptions import APIException

from drf_spectacular.utils import extend_schema


# Dashboard View
@extend_schema(
  tags = ['Dashboard'],
  
  responses = {200: DashboardSerializer (many = True)},
)
class DashboardListView(ListAPIView):
    
    queryset = Dashboard.objects.all()
    
    serializer_class = DashboardSerializer
    
    permissions_classes = [IsAuthenticated]
    
@extend_schema(
  tags = ['Dashboard'],
  
  responses = {201: DashboardSerializer (many = True)},
)  
class DashboardCreateView(CreateAPIView):
    
    queryset = Dashboard.objects.all()
    
    serializer_class = DashboardSerializer
    
    permission_classes = [IsAuthenticated]
    
# Handle exception

    def post(self, request,*args,**kwargs):
        try:
            return super().post(request,*args,**Kwargs)
        except Exception as e:
            raise APIEXCEPTION ('error creating dashboard')
    
# add validation

    def validate_name(self, value):
        if not value:
            raise validators.ValidationError('Name is required')
        return value
        

    
# User View   
@extend_schema(
  tags = ['User'],
  
  responses = {200: UserSerializer (many = True)},
)
class UserListView(ListAPIView):
    
    queryset = User.objects.all()
    
    serializer_class = UserSerializer
    
    permissions_classes = [IsAuthenticated]
    
  
@extend_schema(
  tags = ['User'],
  
  responses = {201:UserSerializer (many = True)},
)      
class userCreateView(CreateAPIView):
    
    queryset = User.objects.all()
    
    serializer_class = UserSerializer
    
    permissions_classes = [IsAuthenticated]




# Widget View
@extend_schema(
  tags = ['Widget'],
  
  responses = {200:WidgetSerializer (many = True)},
)
class WidgetListView(ListAPIView):
    
    queryset = Widget.objects.all()
    
    serializer_class = WidgetSerializer
    
    permissions_classes = [IsAuthenticated]
 
@extend_schema(
  tags = ['Widget'],
  
  responses = {201:WidgetSerializer (many = True)},
)       
class WidgetCreateView(CreateAPIView):
    
    queryset = Widget.objects.all()
    
    serializer_class = WidgetSerializer
    
    permissions_classes = [IsAuthenticated]
    
    
