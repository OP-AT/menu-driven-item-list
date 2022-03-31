print("om")
a= {}
i = 1
l= []
def yes(a, l):
    d= {}
    b= int(input("enter item code: "))
    d["name"] = str(input("enter item name here: "))
    d["price"] = int(input("enter price here: "))        
    a[b] = d
    l.append(d["price"])

while 1>0:
    ch= str(input("do you want to enter an item? : "))
    if ch == "yes":
        yes(a, l)
    elif ch == "no":
        print("your item list :- ", a)
        break
print("menu")
print("to print the info of the costliest item press 1")
print("to search for an item press 2")
print("to add more item press 3")
print("to remove an item press 4")
print("to exit press 5")

i = 1
while 2>1:
    c= int(input("enter ur choice here: "))
    if c == 1:
        l.sort
        for i in a:
            if a[i]["price"] == l[-1]:
                print(a[i]["name"], "is the costliest item")                
    elif c ==2:
        m= str(input("enter item name here to search: "))
        for i in a:
            if a[i]["name"]== m:
                print(m, ": ", {"item code ": i, "price ": a[i]["price"]})
    elif c == 3:
        d= {}
        b= int(input("enter item code: "))
        d["name"] = str(input("enter item name here: "))
        d["price"] = int(input("enter price here: "))        
        a[b] = d
        l.append(d["price"])
        print("the edited list is : ", a)
    elif c== 4:
        v = str(input("enter the name of item u want to remove: "))
        for i in a:
            if a[i]["name"] == v:
                del a[i]
                break
        print(a)
    elif c == 5:
        break



    