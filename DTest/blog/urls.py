from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
""" . means here import from current packages """
from . import views


""" 
	Here if we don't close first reguler expression then it will always go blog home page
	if nevigation is this "blog/1" because "blog/" takes you to home
"""
urlpatterns = [
    url(r'^blog/$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
    	template_name="blog/home.html")),
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name= 'blog/post.html')),
]