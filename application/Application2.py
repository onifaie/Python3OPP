import random # this import labrary to chooes random Number 

class thinkingNumber:
   
        def __init__(self):
            #save random nmber inside varable secritnumber 
            self.secritNumber=random.randint(1,3)
            self.fun()# this call funcation name id fun 
           
        def fun(self):
        
            # this msg to use to chooes number bettwen tow number 
            print(" I am thinking of number bettwen 1 - 3 ")
            for guesesTaken in range(1,3):
                print (" Take a quss ")
                quess=int(input())
                if quess < self.secritNumber:
                    print (" you quess is low ")
                elif quess > self.secritNumber:
                    print(" your quess is too larg ")
                else:
                    break
                
            if quess==self.secritNumber:
                print("Good jop you quess my number in "+ str(guesesTaken) + "quess !")
            else :
                print (" Nop the Number I was thinking of was  " + str(self.ecritNumber) )
            
c1=thinkingNumber()
c1.fun()
    