class myobeid:
    
    def myfun(self,x,y):
        value=int(input("Enter the Number of choice "))
        if value==1:
            result=x+y
            return result
        if value==2:
            result=x*y
            return result
        if value==3:
            result=x/y
            return result
        if value==4:
            result=x**y
            return result
        if value>=5:
            print(" please choiec Number  1 To 4 ")
        
        
        
c1=myobeid()
print(c1.myfun(5,6))

            
            