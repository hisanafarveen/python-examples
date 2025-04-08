list12=["suhana","fasmina","asba"]
for value in list12:
    print (value[::-1])
    
def print(value):
    return (value[::-1])
list(map(print,list12))

list(map(lambda value:value[::-1],list12))

list14=["dilba","rinsha","farhana"]  
for value in list14:
    print(value[::-2])  
list3=[12,34,67,64,13,17] 
sum=0 
for value in list3:
    sum+=value
    print(sum)
    
def print(a,b):
    return a+b
from functools import reduce
reduce(print,list3)

reduce(lambda a,b:a+b,list3)

list10=[10,5,8,15,19,40]
    
def print(a,b):
    return a*b
from functools import reduce
reduce(print,list10)
reduce(lambda a,b:a*b,list10)

list33=[10,20,30,40,50,123,567]
def highestnumber(a,b):
    if a>b:
        return a
    else:
        return b
    
reduce(highestnumber,list33)
reduce(lambda a,b:a if a>b else b,list33)