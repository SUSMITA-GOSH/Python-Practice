# Result={
#     "Exam" : "hsc",
#     "Gpa" : "A+",
#     "tup":("java","python","c",'c++'),
#     "Marks" :{
#         "phy" : 96,
#          "che" : 98,
#           "bio" : 98,
#            "math" : 100,
#             "bangla" : 95,
#     }
    
    
    
# }
# print(Result)
# print(Result["Marks"])

# print(Result["Marks"]["math"])

# print(list(Result.keys()))
# print(len(list(Result.keys())))

# print(Result.items())
# print(list(Result.items()))
# print(Result.get("tup"))
# new_dict={
#     "Admission ":"Gst",
#     "Mark":77}
# Result.update(new_dict)
# print(Result)
# sub={}
# x=int(input("phy :"))
# sub.update({"phy ": x})
# y=int(input("che :"))
# sub.update({"che ": x})
# x=int(input("math :"))
# sub.update({"math ": x})
# x=int(input("bio :"))
# sub.update({"bio ": x})
# print(sub)

# capital={"Bnagladesh":"Dhaka",
#          "India":"Delhi",
#          "Thailand":"bangkok",
#          "usa":" washington dc",
#          "China":"Beijing"
         
    
# }
# items=capital.items()
# print(items)
# for key,value in capital.items():
#     print(f"{key} : {value}")
  

# print(capital.get("India"))
# print(capital.get("China"))
# if capital.get("japan"):
#     print("exists")
# else:
#     print("Not exists")
    
    
    
    
  #Concession stand program
  
Menu = {
    "Momos": 180,
    "MEATBOX": 200,
    "chowmin": 200,
    "Thai soup": 200,
    "Wings": 280,
    "Coffe": 360,
    "NACHOS": 250,
    "Rice": 200,
    "pizza": 700
}

cart = []
total = 0

# Display the menu
print("----- MENU -------")
for key, value in Menu.items():
    print(f"{key:10} : {value} TK")
print("------------------")

# Take user orders
while True:
    food = input("Select an item (q to quit): ").strip().lower()
    if food == "q":
        break
    elif food in [item.lower() for item in Menu.keys()]:
        cart.append(food)
    else:
        print("Item not available. Please select from the menu.")

# Display the order
print("\n------ Your Order ------")
print(f"{'Item':15} {'Price (TK)':10}")
print("-" * 25)

for x in cart:
    for key in Menu.keys():
        if x == key.lower():
            price = Menu[key]
            print(f"{key:15} {price:10}")
            total += price

# Display the total with tax
taxed_total = total + total * 0.02
print("-" * 25)
print(f"{'Total (with tax)':18} {taxed_total:10.2f} TK")
