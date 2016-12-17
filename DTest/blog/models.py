from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=140) 
	body = models.TextField()
	date = models.DateTimeField()

	""" To get String our of title object we need to write getter for this field """
	def __str__(self):
		return self.title