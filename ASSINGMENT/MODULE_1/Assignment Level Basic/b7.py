#B7. Write a Python program to check if variable is of integer or string.
b="meet"

type1=type(b)
print(type1)
if type1==int:
    print("this is int")
elif type1==str:
    print("this is str")
