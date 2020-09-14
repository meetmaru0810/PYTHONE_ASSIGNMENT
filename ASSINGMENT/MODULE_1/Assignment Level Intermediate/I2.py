#I2:- Write a Python program to find whether a given number is even or odd,
#print out an appropriate message to the user
i=int(input("enter the no to find even or odd:"))
if i<0:
    print("invalid no")
elif i%2==0:
    print("entered no is even")
elif i%2!=0:
    print("entered no is odd")