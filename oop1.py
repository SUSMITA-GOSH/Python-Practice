class Student:
    ex = "student database :"
    uni = "SUST"
    
    def __init__(self, name, roll, section, department):
        self.name = name
        self.roll = roll
        self.section = section
        self.department = department
    
    def welcome(self):
        print("welcome student", self.name)
     
# Creating an instance of the Student class
s1 = Student("Susmita", 29, "A", "CSE")
s1.welcome()

# Accessing class attributes through the class name
print(Student.uni)
print(Student.ex)

# Printing the attributes of the instance
print("Name=" + s1.name, "Roll=" + str(s1.roll), "Section=" + s1.section, "Department=" + s1.department)

# Creating another instance of the Student class
s2 = Student("Eipa", 8, "A", "Mathematics")
print(s2.name, s2.roll, s2.section, s2.department)
