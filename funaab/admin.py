from django.contrib import admin
from .models import Course, Question, Department, Upvote, College, Answer, Post, Discussion, Report, DiscussionUpdateTable
# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Department)
admin.site.register(Answer)
admin.site.register(Upvote)
admin.site.register(Post)
admin.site.register(Report)
admin.site.register(Discussion)
admin.site.register(DiscussionUpdateTable)