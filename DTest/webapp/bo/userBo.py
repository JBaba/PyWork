from webapp.models import User
from datetime import datetime

class UserBo:
     
    """ To get String our of title object we need to write getter for this field """
    def __str__(self):
        return "UserBo[  ]" 
    
    """ Create User from passed parameters """
    def createUser(self,request):
        loginUser = User()
        loginUser.username = request.POST.get('USERNAME')
        loginUser.password = request.POST.get('Password')
        loginUser.date = str(datetime.now())
        loginUser.save()
        
    """ return true is any user exits in database if not then return false """
    def isAnyUserExits(self):
        return False if User.objects.all().__len__() == 0 else True
   
    def printNoOfUsersExits(self):
        print "No of user in database : " , User.objects.all().__len__() 