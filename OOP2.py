
# this Code about how play with cimputer chooes Number Gusst Number Buttwen 0 to 20 
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
        
        
c1=RnadomNumber()
c1.Qusttnumber()
