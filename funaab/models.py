from django.db import models

# Create your models here.


class College(models.Model):
  college_name = models.CharField(max_length=200, blank=True)
  def __str__(self):
  	return self.college_name


class Department(models.Model):
  department_name = models.CharField(max_length=200, blank=True)
  college = models.ForeignKey(College,null = True, on_delete=models.CASCADE)
  def __str__(self):
  	return self.college_name


class User(models.Model):
    first_name = models.CharField(max_length=200, help_text='Your first name')
    last_name = models.CharField(max_length=200, blank=True)
    user_name = models.CharField(max_length=50, unique=True)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    matric_number = models.IntegerField(blank=True, default= 0)
    
    def set_password(self, raw_password):
    	self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
    	from django.contrib.auth.hashers import check_password
    	return check_password(raw_password,self.password)

    def __str__(self):
        return self.user_name


class Course(models.Model):
    course_name = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Question(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    academic_session = models.IntegerField(default=0)
    question_text = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)
    answer_file = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question_text[:50]


class Upvote(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now= True)

class Report(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    report_response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.content[:50]


class DiscussionUpdateTable(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null = True,on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)