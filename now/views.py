from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def current_projects(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'now/current_projects.html', {'posts': posts})

def index(request):
    return render(request, 'now/index.html', {})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'now/project_detail.html', {'post': post})