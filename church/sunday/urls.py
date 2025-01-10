from django.urls import path
from . import views

urlpatterns = [
    path('sunday/', views.sunday_school_list, name='sunday_school_list'),
    path('sunday/<int:lesson_id>/', views.sunday_school_detail, name='sunday_school_detail'),
]
