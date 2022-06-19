# this Test File 
from operator import indexOf
from xml.dom.pulldom import START_DOCUMENT
'''
this class about  read the list and added it to another list  by one by one  to abther list 
then  added and print so call the funcation to do it 
'''
class Student:
    studentslist=[99]
    mylist=[2,4,6,8]
    def addstudent(self):
        '''
        thsi for loop to add element to my list one by one 
        '''
        for i in self.mylist:
            i+=i # this add the seam number to i elment inside mylist 
            mylist=self.studentslist.append(i)
            
        
        
       
        print(self.studentslist)
       
    

c1=Student() # take instans from your class 
c1.addstudent() # call instant class Student  to do the function  addstudent 

        