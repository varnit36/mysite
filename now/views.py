from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext
def current_projects(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'now/current_projects.html', {'posts': posts})

def index(request):
    return render(request, 'now/index.html', {})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'now/project_detail.html', {'post': post})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
