#B11:- Write a Python program to get the Fibonacci series of given range
no=int(input("range of fibonaci series:"))
a1,a2=0,1
print("fibonacci no",a1)
print("fibonacci no",a2)
for i in range(2,no+1):
    a3=a1+a2
    print("fibonacci no",a3)
    a1=a2
    a2=a3