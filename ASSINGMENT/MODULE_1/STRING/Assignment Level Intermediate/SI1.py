# I1.Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

s1="qwe"
s2="wer"
print(s1,s2,end=" ")
s11=s2[:2]+s1[2]
s22=s1[:2]+s2[2]
print(s11,s22,end=" ")