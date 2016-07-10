from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from portfolio.utils import get_data
from django.utils import timezone
from portfolio.utils import generate_profile_image, generate_username, filter_comment
from django.core.urlresolvers import reverse

from .models import Comment

# Create your views here.
def index(request):
	comment_list = Comment.objects.filter(parent=None).order_by('date')
	context = {'comment_list': comment_list}
	return render(request, 'portfolio/index.html', context)

def addcomment(request):
	text = request.POST['newcomment']
	c = Comment(content = filter_comment(text), date=timezone.now(), image = generate_profile_image(), username = generate_username())
	c.save()
	comment_list = Comment.objects.filter(parent=None).order_by('date')
	context = {'comment_list': comment_list}
	return HttpResponseRedirect(reverse('index'))
	# return render(request, 'portfolio/index.html', context)

def addchildcomment(request, comment_id):
	text = request.POST['newchildcomment']
	c = Comment(content = filter_comment(text), date=timezone.now(), image = generate_profile_image(), username = generate_username(), parent = Comment.objects.get(pk=comment_id))
	c.save()
	comment_list = Comment.objects.filter(parent=None).order_by('date')
	context = {'comment_list': comment_list}
	return HttpResponseRedirect(reverse('index'))

def startproject(request):
	project_data = get_data()
	context = {"assign_name": "Assignment 0", "project_name": "Bring Your Code", 
		"d": project_data['Assignment0'], 'file_list': project_data['Assignment0']['files']}
	return render(request, 'portfolio/detail.html', context)

def chess(request):
	project_data = get_data()
	context = {"assign_name": "Assignment 1", "project_name": "Chess", 
		"d": project_data['Assignment1'], 'file_list': project_data['Assignment1']['files']}
	return render(request, 'portfolio/detail.html', context)

def csair(request):
	project_data = get_data()
	context = {"assign_name": "Assignment 2", "project_name": "CS Air" , 
		"d": project_data['Assignment2'], 'file_list': project_data['Assignment2']['files']}
	return render(request, 'portfolio/detail.html', context)

def webportfolio(request):
	project_data = get_data()
	context = {"assign_name": "Assignment 3", "project_name": "Web Portfolio" , 
		"d": project_data['Assignment3'], 'file_list': project_data['Assignment3']['files']}
	return render(request, 'portfolio/detail.html', context)

					