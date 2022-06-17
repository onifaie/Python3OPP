class Obeid:
    mylist=[3,5,7,8,9]
    
    newlist=[]
    def addnumber(self,x,y):
        
        self.newlist.append(x)
        print("--------------")
        print(self.newlist)
        self.mylist.append(self.newlist)
        print (x+y)
        print(self.newlist)
        
    def myfunctionobeid(self,f):
        for i in range(1,f,3):
            print (f"this my number is {i} iside the loop ")
        
class Obeid2(Obeid): # this class inhites from frist class ( class Obeid ) all funcation can use it 
    # this inhirts class from another call 
    
    def msgobeid(self,z):
        print(z)
        
        
d=Obeid2() # just call the class 2 ( Obeid 2 )  class Obeid inhirtse   now you can use any function inside class one Obeid 

d.addnumber(55,5)
d.msgobeid("Hi are you ok today !!!!")
d.addnumber(30,10)
d.myfunctionobeid(30)

