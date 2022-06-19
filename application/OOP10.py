class myclass:
    def muiltable(self,start,end,fr,st):
        start=int(input("enter the start no "))
        end =int(input("Enter the End No "))
        fr=int(input("enter the from "))
        st=int(input("enter the end "))
        
        for x in range(start,end+1):
            
            for y in range(fr,st+1):
                print(f"{x }*{ y}  = : {x*y}")
            print("==================")

                
c1=myclass()
c1.muiltable(5,10,1,11)

![obeid!](app.png)