from django.urls import path
from . import views

urlpatterns = [
    path('', views.sunday_list, name='sunday_list'),
    path('<int:lesson_id>/', views.sunday_detail, name='sunday_detail'),
]
