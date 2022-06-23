import random # this import library to choose random Number 

class thinkingNumber:
    '''' this class to include all things inside the class and choose any 
    any function 
    '''
   
    def __init__(self):
            #save random Number  inside Variable secret_number 
            self.secret_Number=random.randint(1,5)
            self.fun()# this call Function name id fun  function 
            # this begin of function  to start
           
    def fun(self):
        while True :

        
            # this msg to use to chose  number between    tow number 
            print(" I am thinking of number between  1 - 5 ")
            for guess_Taken in range(1,3):
                print (" Take a guess ")
                guess=int(input())
                if guess < self.secret_Number:
                    print (" you guess is low ")
                elif guess > self.secret_Number:
                    print(" your guess is too large ")
                elif guess==self.secret_Number:
                    print(" Good jop ")
                    h=int(input("do you want to play agin  2=yes 1=No "))
                    if h==2:
                        self.secret_Number=random.randint(1,5)
                        
                    elif h==1:
                        print(" See you Soon bye .....")
                        break
                break
                    

                        

                    
              
               
c1=thinkingNumber()
c1.fun(1)