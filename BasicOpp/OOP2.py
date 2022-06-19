#This File about practecal  use class and function and looping 
import random
class RnadomNumber:
    '''
    this function ask user to Gusst Number Buttwen 0 to 20  if his chooes write print good lock 
    anther wis  print Sorry your wrong Number Try agin !!!!!
    '''
    def Qusttnumber(self):
        t=input("Enter your Number you Qusst ")
        y=random.randint(0,20) 
        if int(t)==y:
            print ("good lock ")
        else:
            print("Sorry your wrong Number try agin ")
            
            
    def singup(self,d):
        print(d)
            
class formating:
    def format(self):
        print("--------------------")


'''this class ingitice from tow class and you can call any function inside all class inhierts '''            
class opration(formating,RnadomNumber):
    def addnumber(self,x,y):
        print (x+y)
    def apstrac(self,x,y):
        print (x*y)
    def pusls(self,x,y):
        print (x/y)
    def Modfun(self,x,y):
        print (int(x)%int(y))
    

        
        
        
c1=RnadomNumber()
c1.Qusttnumber()

oneclass=opration()
oneclass.addnumber(3,4)
oneclass.format()
oneclass.apstrac(5,6)
oneclass.format()
oneclass.pusls(4,5)
oneclass.format()
oneclass.Modfun(12,5)

c2=opration()
c2.singup("this my name obeid thanks !!!!!!!!!!")

