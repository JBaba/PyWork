from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>Hi There!</h2>")

def login(request):
	return render(request,'webapp/login.html')

def dologin(request):
	print('i am in do login')
	print(request.method)
	print(request.POST)
	
	for key, value in request.POST.iteritems():
		print(key , value)
	
	return render(request,'webapp/login.html',{})
