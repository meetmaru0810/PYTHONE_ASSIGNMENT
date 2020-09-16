name=input("enter the name:")
age=int(input("enter the age:"))
gender=input("enter the gender male=m and female=f:")

purchase=int(input("enter the purchase amount:"))

if age>65:

    if gender=="m":
        if purchase>25000:
            discount=(purchase*25)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        elif purchase>50000:
            discount=(purchase*50)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        else:
            print("no discount")
    elif gender=="f":
        if purchase>25000:
            discount=(purchase*30)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        elif purchase>50000:
            discount=(purchase*55)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        else:
            print("no discount")
elif age<65:
    if gender=="m":
        if purchase>25000:
            discount=(purchase*20)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        elif purchase>50000:
            discount=(purchase*40)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        else:
            print("no discount")
    elif gender=="f":
        if purchase>25000:
            discount=(purchase*25)/100
            print(name,"your purchase amount is",purchase,"discount is",discount)
        elif purchase>50000:
            discount=(purchase*50)
            print(name,"your purchase amount is",purchase,"discount is",discount)
        else:
            print("no discount")



