num=int(input("Enter a number between 1-10 "))
while num<1 and num<10:
    print(f"{num} is not valid")
    num=int(input("Enter a number between 1-10"))
print(f"you num is {num}")


#PYTHON COMPOUND INTEREST CALCULATOR
Principle =0
rate=0
time=0


while True:
    Principle=float(input("Enter the Priciple amount :"))
    if Principle<0:
      print("principle  less then zero")
    else:
        break

while True:
    rate=float(input("Enter the interest rate amount :"))
    if rate<0:
      print("interest rate less then zero")
    else:
        break

while True:
    time=float(input("Enter the time :"))
    if time<0:
      print("time can't less than zero")
    else:
        break
    
total=Principle*pow((1+rate/100),time)
print(f"Balance after {time} years with interest {rate} is : Tk {total:.2f} ")