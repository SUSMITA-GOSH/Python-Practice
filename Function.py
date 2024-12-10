import time
def display_invoice(user,amount,due):
    print(f"Hello {user}")
    print(f"Your bill of Tk-{amount} is due {due}")
    
display_invoice("kkkk",5678,"01/09")

def name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

full_name=name("susmita","gosh")
print(full_name)


def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done")
    
count(10)
#KEYWORD
