# A3:- Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero.


a=int(input("enter the no1:"))
b=int(input("enter the no2:"))
c=int(input("enter the no3:"))

if a==b or a==c or b==c:
    print("sum of three no is=0")
else:
    d=a+b+c
    print("sum of three no is=",d)