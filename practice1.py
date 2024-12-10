class Student:
    def __init__(self,name,phy,che,bio):
        print("result")
        self.name=name
        self.phy=phy
        self.che=che
        self.bio=bio
    @staticmethod
    def welcome():
        print("Good Luck")
        
    def avg(self):
        
       
        
        avg=(self.phy+self.che+self.bio)/3
        return avg
    
s1= Student("susmita",98,96,98)

print(s1.name, s1.phy, s1.che, s1.bio)
print("Average:", s1.avg())
s1.welcome()
