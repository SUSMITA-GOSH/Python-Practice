a=int(input("a="))
b=int(input("b="))
sum=a+b
print(type(a))
print(sum)
print(a/b)
print(a**a)
num=input("num=")
print(type(num))
num2=input("num2=")
print(num+" "+num2)
num1=num+" "+num2
print(len(num1))
print(num1[0:7])
print(num1[-7:])
#String
str="i am a useless person"
print(str.endswith("on"))
print(str.capitalize())
print(str.upper())
print(str.replace("useless","lazy"))
print(str.find("o"))#first occurance
print(str.rfind("s"))#last occurance
print(str.count("a"))
name=input("what is your name")
print(f"hello {name} !")
credit="123-345-6876889"
c=credit[::-1]#print reverse
print(c)