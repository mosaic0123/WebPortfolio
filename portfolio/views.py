from django.shortcuts import render
from django.http import HttpResponse
from portfolio.utils import get_data

# Create your views here.
def index(request):
	return render(request, 'portfolio/index.html')

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

					