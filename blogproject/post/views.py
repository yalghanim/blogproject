from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .forms import PostForm, UserSignUp, UserLogIn

from django.contrib import messages
from django.http import Http404, JsonResponse
from django.utils import timezone 
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout 

def like_button(request, post_number):
	obj = Post.objects.get(id= post_number)

	like, created = Like.objects.get_or_create(user= request.user, post=obj)
	if created:
		action="like"
	else:
		action="unlike"
		like.delete()
	post_like_count = obj.like_set.all().count()
	response = {
		"action": action,
		"like_count": post_like_count,
	}
	
	return JsonResponse(response, safe=False)

def userlogout(request):
    logout(request)
    return redirect("posts:list")

def userlogin(request):
	context = {}
	form = UserLogIn()
	context['form'] = form
	if request.method == "POST":
		form = UserLogIn(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("posts:list")
			else:
				messages.error(request, "Wrong Combinations. Please try again.")
				return redirect("posts:login")
		else:
			message.warning(request, form.errors)
			return redirect("posts:login", request)
	
	return render(request, 'login.html', context)




def usersignup(request):
	context = {}
	form = UserSignUp()
	context['form'] = form
	if request.method == "POST":
		form = UserSignUp(request.POST)
		if form.is_valid():
			user = form.save(commit=False) #so we can retrieve the object
			username = user.username
			password = user.password
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)
			return redirect("posts:list")
		else:
			messages.error(request, form.errors)
			return redirect("posts:signup")

	return render(request, 'signup.html', context)



def home(request):
	return HttpResponse("<h1> شغال </h1><br><br><h3>THIS STUFF IS EASY</h3>")
def post_create(request):
	return HttpResponse("<h1>create</h1>")
def post_update(request):
	return HttpResponse("<h1>update</h1>")
def post_delete(request):
	return HttpResponse("<h1>delete</h1>")

def post_list(request):

	today = timezone.now().date()
	post_list = Post.objects.filter(draft=False).filter(publish__lte=today)
	if request.user.is_staff or request.user.is_superuser:
		post_list = Post.objects.all()
	post_one = Post.objects.get(title="edited name")
	query = request.GET.get("q")
	if query:
		post_list = post_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(author__first_name__icontains=query)|
			Q(author__last_name__icontains=query)|
			Q(author__username__icontains=query)
			).distinct()

	context = {
	"title": "(this is taken from the context)",
	"user": request.user,
	"post_list": post_list,
	"post_one": post_one,
	"today": today,
	}
	return render(request, 'newlist.html', context) 

def new_list(request):
	post_list = Post.objects.all()
	context = {
	"post_list": post_list,
	}
	return render(request, 'newlist.html', context) 

def post_id(request, slug):
	obj = get_object_or_404(Post, slug=slug)
	date = timezone.now().date()
	if obj.publish > date or obj.draft:
		if not(request.user.is_staff or request.user.is_superuser):
			raise Http404

	if request.user.is_authenticated():
		if Like.objects.filter(post= obj, user= request.user).exists():
			liked = True 
		else:
			liked = False 

	post_like_count = obj.like_set.all().count()

	context = {
	"input": obj,
	"liked": liked,
	"like_count": post_like_count,
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

def post_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save(commit=False)
		obj.author = request.user
		obj.save
		messages.success(request, "Mabroooooook!!!!!")
		return redirect("posts:list")
	context = {
		"form":form,
	}
	return render(request, 'form.html', context)

def post_update(request, slug):
	if not (request.user.is_superuser):
		raise Http404
	post_object = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "zain sawait")
		return redirect("posts:list")
	context = {
		"form": form,
		"post_object": post_object,
	}
	return render(request, 'update.html', context)

def post_delete(request, slug):
	if not (request.user.is_superuser):
		raise Http404
	Post.objects.get(slug=slug).delete()
	messages.warning(request, "Haram alaik")
	return redirect("posts:list")
