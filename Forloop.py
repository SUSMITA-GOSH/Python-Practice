import time
# list=(12,34,6,7,987,665,44,5,5,78,9,9,0)
# x=5
# ind=0
# for num in list:
#   if( num==x):
      
#       print("x found ",ind)
     
#       ind+=1
# for i in range(5):#range(start,stop,increment)
#     print(i)
# for i in range(10,100,5):
#     print(i)
#     time.sleep(3)
# n=int(input("n="))
# fact=1
# i=1 
# while(i<=n):
#   fact*=i
#   i+=1
#   print(fact)
# def calc(a,b):  
#   return a+b
# sum=calc(4,6)
# print(sum)
# Stop watch
# times=int(input("enter the seconds"))
# for x in range(times,0,-1):
#   second=x%60
#   min=int((x/60)%60)
#   hour=int(x/3600)
#   print(f"{hour:02} : {min:02} : {second:02}")
#   time.sleep(1)
# print("Times up!")


row=int(input("Enter the row "))
col=int(input("enter the col "))
for i in range(row):
    for j in range(col):
      if i == 0 or i == row - 1 or j == 0 or j == col - 1 or i==j:
            print("*", end="")
      else:
            print(" ", end="")
    print()
        
    
