from django.shortcuts import render
from rest_framework import generics
from .models import Course, Department, Question, Answer, College, Upvote, Report, Post, Discussion,User
from .serializers import CourseSerializer, DepartmentSerializer, QuestionSerializer, AnswerSerializer, UpvoteSerializer, ReportSerializer, PostSerializer, UserSerializer, DiscussionSerializer
# Create your views here.

class CourseListView(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	
class CourseCreateView(generics.CreateAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveAPIView):
	lookup_field = 'id'
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class CourseUpdateView(generics.RetrieveUpdateAPIView):
	lookup_field = 'id'
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class CourseDestroyView(generics.DestroyAPIView):
	lookup_field = 'id'
	queryset = Department.objects.all()
	
class DepartmentListView(generics.ListAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	
class DepartmentCreateView(generics.CreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	
class QuestionListView(generics.ListAPIView):
	queryset = Department.objects.all()
	serializer_class = QuestionSerializer
	
class QuestionCreateView(generics.CreateAPIView):
	queryset  = Department.objects.all()
	serializer_class = QuestionSerializer
	
class AnswerListView(generics.ListAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
	
class AnswerCreateView(generics.CreateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
	
class PostCreateView(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class ReportCreateView(generics.CreateAPIView):
	queryset = Report.objects.all()
	serializer_class = ReportSerializer

class DiscussionCreateView(generics.CreateAPIView):
	queryset = Discussion.objects.all()
	serializer_class= DiscussionSerializer

class UserCreateView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UpvoteCreateView(generics.CreateAPIView):
	queryset = Upvote.objects.all()
	serializer_class = UpvoteSerializer

	