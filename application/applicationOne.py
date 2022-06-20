class Myclass:
    def Mfun(self,start,end,Sfrom,Efrom):
        for x in range(start,end+1):
            for y in range(Sfrom,Efrom):
                print(f"{x}*{y} = {x*y}")
            print("=====================")
    
    def countThewords(self,sentince):
        mywords=sentince.split()
        print (len(mywords))
        def __init__(self):
            print('''
          
    Please chooes Number To Play Games : 
        1- Play game MulitTable 
        2- A count of words 
        3 - To Play agine 

              
              ''')
        while True :
          Number=int(input("please Chooes the Number "))
          if Number==1:
            self.Mfun(3,5,1,3)
          if Number==2:
              words=input(" Enter your sentuincs  here ")
              self.countThewords(words)
          if Number==3:
              print ("coohes 3")

c1=Myclass()
