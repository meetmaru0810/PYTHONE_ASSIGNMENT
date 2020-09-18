#A2.Write a Python program to get a string from a given string where all occurrences
#of its first char have been changed to '$', except the first char itself
s1="MEET MARU"
v=s1[0]
print(v)
s1=s1.replace(v,"$")
print(s1)
s1=v+s1[1:]
print(s1)