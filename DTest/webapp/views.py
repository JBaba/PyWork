from django.shortcuts import render
from django.http import HttpResponse
from webapp.forms.login import submitLogin
from django.http.response import HttpResponseRedirect
from .models import User
from webapp.bo.userBo import UserBo

def index(request):
	return HttpResponse("<h2>Hi There!</h2>")

def login(request):
	return render(request,'webapp/login.html')

def dologin(request):
	if request.method == 'POST':
		print('Login Username : ',request.POST.get('USERNAME'))
		userBo = UserBo()
		userBo.printNoOfUsersExits()
		if userBo.isAnyUserExits() :
			userBo.createUser(request)
	
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
