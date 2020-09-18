# I3.Write a Python program to find the first appearance of the substring 'not'
# and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

s="The lyrics is not that poor!"
print(s)
s1=s.find("not")
s2=s.find("poor")
print(s1)
print(s2)
if s1<s2 and s1>0 and s2>0:
    s3=s.replace(s[s1:(s2+4)],"good")
    print(s3)