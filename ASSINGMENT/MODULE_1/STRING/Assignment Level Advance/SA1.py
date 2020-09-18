"""A1.Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the empty string.
Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String """


s1=input("enter the string:")
l=len(s1)
if l<2:
    print("empty string")
elif l==2:
    s2=s1[0:2]+s1[0:2]
    print(s2)
else:
    s3=s1[0:2]+s1[-2:]
    print(s3)
