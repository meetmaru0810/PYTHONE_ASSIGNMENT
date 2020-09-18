#I5. Write a Python function to reverses a string if it's length is a multiple of 4

s=input("enter the string:")
if len(s)%4==0:
    v=s[::-1]
    print(v)
else:
    print(s)