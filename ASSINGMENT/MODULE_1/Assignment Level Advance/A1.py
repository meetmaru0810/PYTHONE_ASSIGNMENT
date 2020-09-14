#A1:- Write a Python program to sort three integers without using
#conditional statements and loops

a=int(input("enter the no1:"))
b=int(input("enter the no2:"))
c=int(input("enter the no3:"))

min1=min(a,b,c)
print(min1)
max1=max(a,b,c)
print(max1)

middle=a+b+c-min1-max1
print(middle)
print("no is in sorted manner=",min1,middle,max1)