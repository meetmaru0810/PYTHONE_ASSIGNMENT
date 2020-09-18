#B6. Write a Python program to count occurrences of a substring in a string
import re
txt="my name  my is meet"
x=re.subn("my","my",txt)
print(x)