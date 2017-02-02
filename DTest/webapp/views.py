from django.shortcuts import render
from django.http import HttpResponse
from webapp.forms.login import submitLogin
from django.http.response import HttpResponseRedirect
from .models import User
from webapp.bo.userBo import UserBo
from django.template.context_processors import request

def index(request):
	return HttpResponse("<h2>Hi There!</h2>")

def login(request):
	return render(request,'webapp/login.html')

def pageSignup(request):
	return render(request,'webapp/signup.html')

def dologin(request):
	if request.method == 'POST':
		print('Login Username : ',request.POST.get('USERNAME'))
		userBo = UserBo()
		userBo.printNoOfUsersExits()
		if not userBo.isAnyUserExits() :
			userBo.createUser(request)
		
		if userBo.isValidUser(request.POST.get('USERNAME'), request.POST.get('Password')):
			print "Valid User"
			return render(request,'webapp/header.html')
		else:
			print "Not Valid User"
			return render(request,'webapp/login.html',{'error_msg':'Not Valid User'})	
	
def addUser(request):	
	userBo = UserBo()
	if request.method == 'POST':
		if userBo.isUserExits(request.POST.get('USERNAME')) :
			return render(request,'webapp/signup.html',{'error_msg':'User already exits'})	
		else:
			userBo.createUser(request)
			return render(request,'webapp/signup.html',{'error_msg':'User has been created'})	

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
