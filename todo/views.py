from django.shortcuts import render
from .models import Tag

def home(request):
    return render(request, 'todo/home.html')

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'todo/tag_list.html', {'tags': tags})