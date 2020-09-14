#A5:- Write a python program to sum of the first n positive integers
n=int(input("enter the no:"))
sum1=0
if n>0:
    for i in range(1,n+1):
        sum1=sum1+i
    print("sum of n no=",sum1)
else:
    print("invalide input")