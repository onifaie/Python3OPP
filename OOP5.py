class Emp:
    def __init__(self,fname,mname,lname):
        
        self.fname=fname
        self.mname=mname
        self.lname=lname
        
       
    
    def myfullname(self):
        fullname=f"{self.fname}-{self.mname}-{self.lname}"
        
        print(fullname)
    
    
    
c1=Emp("obeid","abduallah","alotibi")
c1.myfullname()
    
    