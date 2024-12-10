num=int(input("Num :"))
if(num>=80):
    print("A+")
elif(num>=75 and num<80):
   print("A")
elif(num>=70 and num<74):   
    print("A-")
elif(num>=65 and num<69):   
    print("B+")
else:
    print("Fail")
food=input("Food =")

teste="sweet"    if food=="mango" or food=="gelebi" else "spicy"
print(teste)
salary=int(input("salary="))
tax=salary*(0.1,0.2) [salary>=10000]
print(tax)

num=10
print("positive " if num>0 else "negatve")
