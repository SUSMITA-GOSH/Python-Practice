#tuple
# fruits=("apple","orange",'kiwi',"avocado","kiwi")
# print(fruits)
# print(fruits.index("kiwi"))
#print(fruits.count("kiwi"))


# #SHOPPING CART PROBLEM
# items=[]
# prices=[]
# total=0

# while True:
#     item=input("Enter your item or press q for Quit :")
#     if item.lower()=="q":
#         break
#     else:
#         items.append(item)
#         price=float(input(f"Enter the price for{item} :"))
#         prices.append(price)
# print("-----Your cart-----")
# for x in items:
#  print(x,end=" ")
# print()
# total+=price
# print(f"You total is {total} ")
#TWO D LIST

# vagies=["carrots","potatos","onions"]
# meats=["chicken",'ffish','turkey']
# groceries=[fruits,vagies,meats]
# print(groceries)
# print(groceries[1][2])
# print(groceries[2][0])
# print(groceries[1][2])
# for colllection in groceries:
#     for food in colllection:
#         print(food,end='')
#KEYPAD
num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for x in num_pad:
    for y in x:
        print(y ,end=" ")
    print()