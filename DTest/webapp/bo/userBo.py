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
        print loginUser , " has been created."
        
    """ return true is any user exits in database if not then return false """
    def isAnyUserExits(self):
        return False if User.objects.all().__len__() == 0 else True
   
    def printNoOfUsersExits(self):
        print "No of user in database : " , User.objects.all().__len__() 
        
    def isValidUser(self,__user,__pass):
        listOfUsers = User.objects.filter(username=__user)
        if listOfUsers.__len__() != 0 :
            user = listOfUsers[0]
            if (user.username == __user) & (user.password == __pass):
                return True
            else:
                return False
        else:
            return False
        
    def isUserExits(self,__user):
        listOfUsers = User.objects.filter(username=__user)
        if listOfUsers.__len__() != 0 :
            return True
        else:
            return False