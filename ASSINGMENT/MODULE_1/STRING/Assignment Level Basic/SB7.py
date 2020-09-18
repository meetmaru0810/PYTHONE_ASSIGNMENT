# B7. Write a Python program to count the occurrences of each word in a given sentence
from collections import Counter
s="my name is my meet"
v=s.split()
print(v)
c=Counter(v)
print(c)


