 #A2:- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn
i=int(input("enter the no:"))
a=i*1
print(a)
b=(a*10)+i
print(b)
c=(b*10)+i
print(c)
d=a+b+c
print("i+ii+iii=",d)