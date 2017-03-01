from django.conf.urls import url
""" . means here import from current packages """
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
     url(r'^login/$', views.dologin, name='dologin'),
]
""" Here we are calling method 'index' which is located inside 'views.py' file """
""" We can not write comments inside list """
