from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Course, Question, Department, College,Answer, Upvote, Report, Post, Discussion, DiscussionUpdateTable

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =['id','first_name','last_name','matric_number','level','email','college_id','password','department_id','points']

class Colleges (serializers.ModelSerializer):
	model = College
	fields = ['id','college_id','college_name']
class CourseSerializer(serializers.ModelSerializer):
		class Meta:
			model = Course
			fields = ['id','course_id','course_name','department_name']
		
class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ['id','question','user','course','academic_session','question_text' 'created_at','updated_at']
		
class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ['id','department_name','college']
		
class AnswerSerializer (serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ['id','user','answer','question','user','answer_text','answer_file','created_at', 'updated_at']
		
class UpvoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Upvote
		fields =['id','user','question','answer','created_at']
		
class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = ['id','answer','question','report_response']
		
class DiscussionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discussion
		fields = ['id','user','title','body']
		
		
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['id','discussion','user','content']
		
class UpvoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Upvote
		fields= ['id','user','question','answer']
		
class ReportSerializer(serializers.ModelSerializer):
	model = Report
	fields = ['id','user','answer','question','report_response']
	
	