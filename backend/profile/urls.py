from django.urls import path
from .views import profileDetailView, ProfileListView, ProfileCreateView

urlpatterns = [

   path('v1/', ProfileListView.as_view(),name = 'Profile_list'),
   
   path('v2/', profileCreateView.as_view(), name = 'profile_create'),
   
   path('v3/'ProfileDetailView.as_view(),name = 'profile_detail'),


]