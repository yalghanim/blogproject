from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404

def home(request):
	return HttpResponse("<h1> شغال </h1><br><br><h3>THIS STUFF IS EASY</h3>")
def post_create(request):
	return HttpResponse("<h1>create</h1>")
def post_update(request):
	return HttpResponse("<h1>update</h1>")
def post_delete(request):
	return HttpResponse("<h1>delete</h1>")

def post_list(request):
	post_list = Post.objects.all()
	post_one = Post.objects.get(title="edited name")
	context = {
	"title": "(this is taken from the context)",
	"user": request.user,
	"post_list": post_list,
	"post_one": post_one,
	}
	return render(request, 'list.html', context) 

def post_id(request, post_number):
	obj = get_object_or_404(Post, id = post_number)
	context = {
	"input": obj
	}
	return render(request, 'obj.html', context) 

def post_detail(request):
	return HttpResponse("<h1>detail</h1>")
def post_one(request):
	return HttpResponse("<h1>one</h1>")
def post_more(request):
	return HttpResponse("<h1>more</h1>")
def post_view(request):
	return HttpResponse("<h1>view</h1>")
def post_index(request):
	return render(request, 'ind.html', {})
def post_fourth(request):
	return render(request, 'fourth.html', {})  
 
# Create your views here.
