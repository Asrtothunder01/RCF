from django.shortcuts import render, get_object_or_404
from .models import Sermon

def sermon_details(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    return render(request, 'sermon_details.html', {'sermon': sermon})

def sermon_list(request):
    sermons = Sermon.objects.all()
    return render(request, 'sermon_list.html', {'sermons': sermons})