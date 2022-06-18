# this new File Number 7 about how use Class and function 

class A:
    def __init__(self,name,ago):
        self.name=name
        self.ago=ago
        print(f"{name} {ago}")
        print("=" * 40 )
        
    def myfun(self,name ,ago ):
        print (self.name, self.ago)

d=A("Saleh",99)
d.myfun("obeid",66)
        
    