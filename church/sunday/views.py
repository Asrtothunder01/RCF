from django.shortcuts import render, get_object_or_404
from .models import SundaySchoolLesson

# View for displaying the list of Sunday School lessons
def sunday_list(request):
    # Fetch all lessons from the database
    lessons = SundaySchoolLesson.objects.all()
    
    # Render the list template and pass the lessons as context
    return render(request, 'sunday_list.html', {'lessons': lessons})

# View for displaying a single Sunday School lesson's details
def sunday_detail(request, lesson_id):
    # Fetch the lesson with the given ID, or return a 404 if not found
    lesson = get_object_or_404(SundaySchoolLesson, pk=lesson_id)
    
    # Render the detail template and pass the lesson as context
    return render(request, 'sunday_detail.html', {'lesson': lesson})
