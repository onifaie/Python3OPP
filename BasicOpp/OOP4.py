class Munber:
    '''this function intialies doing when you take instanc class '''
    def __init__(self, *args, **kwargs):
        f=[1,4,7,44,55,33,22,8]
        
        for i in f:
            if i==55:
                continue
            print(i)
        print("this come from init function ")
        
    def add(self,x,y): #this function just add tow number and print the result 
        print(x+y)
    
    



c1=Munber()# this take instanc from class 
c1.add(4,5)#this call function and passing tow pramater 4 , 5 