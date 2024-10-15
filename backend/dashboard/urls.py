from django.contrib import admin

from . import views

from django.urls import path

# dashboard urls

urlpatterns =[
    
    path('dash/list/', views.DashboardListView.as_view(),name = 'list'),
    
    path('dash/create/',views.DashboardCreateView.as_view(), name = 'create'),
    
    path('user/list/',views.UserListView.as_view(),name = 'user_list'),
    
    path('user/create/', views.UserCreateView.as_view(),name = 'create'),
    
    path('widget/list/', views.WidgetListView.as_view(), name = 'list'),
    
    path('widget/create/',views.WidgetCreateView.as_view(), name = 'create'),

]