from django.db import models

class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    date = models.DateTimeField()

    """ To get String our of title object we need to write getter for this field """
    def __str__(self):
        return "User[" + self.username + " " + self.password + " " + str(self.date) + "]" 
