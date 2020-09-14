# name="meet"
# n="my name is %s"%name
# m="my name is %s"
# print(n)
# print(m)

#  *args and **kwargs topic
def function(normal,*a,**kwargs):
    for item in a:
        print(type(a))
        print(item)
    for key,values in kwargs.items():
        print(type(kwargs))
        print(key,values)
    
n=["meet,mihir,prince,zenith,rajdeep"]
normal="my name is meet" 
h={"name":"meet","surname":"maru","leval":"college"}
function(normal,*n,**h) 
    