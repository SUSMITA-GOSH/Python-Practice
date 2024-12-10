class Student :
    class_year=2024
    num_stu=0
    def __init__(self,name,age):
       self.name=name
       self.age=age
       Student.num_stu+=1

student1=Student("spoongbob",30)
student2=Student("patrick",30)
print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_stu)
print(f"My graduating class of {Student.class_year} has {Student.num_stu} students")