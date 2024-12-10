class Animal :
    def __init__(self,name):
        self.name=name
        self.is_alive=True
        
    def eat(self):
        print(f"{self.name} is asleep")
    def sleep(self):
        print(f"{self.name} is sleeping")   

class Dog(Animal):
    def speak(self):
        print("woof woof !!")

class Child(Dog):
    def bark(self):
        print("The dog is barking")


a=Animal("cat")
a.eat()
a.sleep()
b=Dog("dog")
b.eat()
b.sleep()
b.speak()
c=Child("puppy")
c.eat()
c.sleep()
c.speak()
c.bark()
