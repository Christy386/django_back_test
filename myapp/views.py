from django.shortcuts import render
from myapp.models import Post

# Create your views here.
from django.http import JsonResponse

def hello_world(request):
    data = {
        'message': 'Hello, World!'
    }
    return JsonResponse(data)

def add_data(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    data = Post(title=title, content=content)
    data.save()

    return JsonResponse({
        'message': 'post writed in the db',
        'title': title,
        'content': content
    })