# #  Write a Python function that takes a list of words and returns the
# # length of the longest one.

l1=["meet","mihir","zenith"]
l2=[]
for i in l1:
    l2.append((len(i),i))
l2.sort()
print(l2[-1],"this element length is biggest")