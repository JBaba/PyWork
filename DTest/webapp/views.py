from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>Hi There!</h2>")

def login(request):
	return render(request,'webapp/login.html')

# Create your views here.
