#Encapsulation
class User:
    def __init__(self,name,email,password):
        #public
        self.name=name
        #protected - just a naming convention stating discouraged use oustide the class
        self._email=email
        #private - accessible only through member methods
        self.__pass=password
    def disp(self):
        print("Name",self.name)
        print("Email",self._email)
        print("Password",self.__pass)
    def getPass(self):
        return self.__pass
user1=User("manu","manu@gmail.com","manu#345")
print("Name",user1.name)#public accessible outside class
print("Email",user1._email)#protected accessible outside class
#print("Password",user1.__pass) #not accessible
user1.disp()
        
