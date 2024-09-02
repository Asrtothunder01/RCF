from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('course/',views.CourseListView.as_view(),name = 'School_list') ,
    
    path ('course/<int:id>/', views.CourseDetailView.as_view(), name= 'Detail_View'),
    
    path ('course/update/<int:id>/', views.CourseUpdateView.as_view(), name = 'Update _View'),
    
    path('course/delete/<int:id>/',views.CourseDestroyView.as_view(), name = 'Delete'),
    
    path ('course/create/',views.CourseCreateView.as_view(),name ='Create_School_list'),
    
    path ('depart/',views.DepartmentListView.as_view(), name = 'Student_list'),
    
    path('depart/create/',views.DepartmentCreateView.as_view(),name = 'Create_Student_list'),
    
    path('question/',views.QuestionListView.as_view(), name = 'Student_list'),
    
    path('question/create/',views.QuestionCreateView.as_view(), name = 'Create_School_list'),
    
    path ('answer/',views.AnswerListView.as_view(), name = 'Answer_List'),
    
    path('answer/create/',views.AnswerCreateView.as_view(), name = 'Create_Answer_List'),
    
    path('report/create/',views.ReportCreateView.as_view(), name = 'Report'),
    
    path('user/create/',views.UserCreateView.as_view(), name = 'User'),
    
    path('discuss/create/',views.DiscussionCreateView.as_view(),name = 'Discussion'),
]