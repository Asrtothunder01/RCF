from django.urls import path
from . import views

urlpatterns = [
    path('sermon/<int:pk>/', views.sermon_details, name='sermon_details'),
    path('sermons/', views.sermon_list, name='sermon_list'),
]
