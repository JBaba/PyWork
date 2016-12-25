from django.shortcuts import render
from django.http import HttpResponse
from webapp.forms.login import submitLogin
from django.http.response import HttpResponseRedirect
from .models import User
from datetime import datetime

def index(request):
	return HttpResponse("<h2>Hi There!</h2>")

def login(request):
	return render(request,'webapp/login.html')

def dologin(request):
	if request.method == 'POST':
		print('Login Username : ',request.POST.get('USERNAME'))
		users = User.objects.all()
		noOfUsers = users.__len__()
		if noOfUsers == 0 :
			loginUser = User()
			loginUser.username = request.POST.get('USERNAME')
			loginUser.password = request.POST.get('Password')
			loginUser.date = str(datetime.now())
			loginUser.save()
			print loginUser
		print users
		print noOfUsers
	
	return render(request,'webapp/login.html')


def dologinWithForms(request):
	print('i am in do login')
	print(request.method)
	print(request.POST.get('USERNAME'))
	for key, value in request.POST.iteritems():
		print(key , value)
		
	if request.method == 'POST':
		form = submitLogin(request.POST)
		print(form)
		
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = submitLogin()
	
	return render(request,'webapp/login.html',{'form':form})
