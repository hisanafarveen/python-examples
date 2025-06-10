list9=[7,8,9,234,9,12,78,98]
def select (a):
    if a%3==0:
        return True
    else:
        return False
list(filter(select,list9)) 

list10=[12,2,12,34,22,12,14]
def print (a,b):
    return a*b
from functools import reduce
reduce (print,list10)

list3=lambda a :a +10
print(list3(5))

list10=lambda a,b : a*b
print(list10(12,2))
 
list3=lambda a,b: a%b
print(list3(123,6))

thisset=[12,56,89,34,87]
print(len(thisset))
print(type(thisset))
mylist= set (("apple","banana","cherry"))
print(mylist)

import re
pattern='string1'
print(re.search(pattern,'string1'))

patttern="string1r"
list(enumerate(patttern))
for i in range(len(pattern)):
    print(i,pattern[i])
    
a=['Jan',"feb","mar","Apr","May"]
list(enumerate(a,1))
for pos,p in enumerate(pattern,1):
    print(pos,p)

tuple(enumerate(pattern))

print(dict(enumerate("string")))

list1=list(enumerate([1,2,3,4]))
print(list1)

a=["geeks","for","geeks"]
for i , name in enumerate(a,2):
    print(f"index{i}: {name}")
print (list(enumerate(a)))  

a=["greek","for","greeks"]
for index,x in enumerate(a,start=1):
    print(index,x)
    
a=["greek","for","greeks"]
for ele in enumerate(a):
    print(ele)  
    
a=["greek","for","greeks"] 
b=enumerate(a,2,1)  
nxt_val=next(b)
print(nxt_val)




import re
txt="the rain is spain"
x=re.search("^the.*spain$",txt)
x
import re 
print('g\n\t*')
print(r'g\n\t*') 
 
import re
pattern=r'[a-z]0?'
print(re.search(pattern,'60b100'))
pattern

pattern=r'10+'
print(re.search(pattern,'abcd100'))

#3.write a python program that machers a string contains a letter followed by zero or one 0's

pattern=r'10{3}'
print(re.search(pattern,'ab1000'))

pattern=r'[a-zA-Z]+_[a-zA-Z]+'
print(re.search(pattern,'aAabc_def_hij'))

#6.check for the pattern dd-mm-yyy"

import re
txt="the rain is spain"
txt1=re.search("the rain is spain", txt)
txt1

import re

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'portal', s)

print('Start Index:', match.start())
print('End Index:', match.end())

pattern=r'[a-zA-Z]+_[A-zA-Z]+'
print(re.search(pattern,'aAabc_def_hij'))

pattern=r'\d{1,2}-\d{1,2}-\d{2,4}'
print(re.search(pattern,'15-04-1996'))

#7.find the words with exactily 8 letters

pattern=r'[a-zA-Z]{18}'
print(re.search(pattern,'pythoninguiyft'))

pattern=r'paython$'
print(re.search(pattern,'this tutorial is about python'))
pattern

pattern=r'\w{7}'
print(re.search(pattern,'this is python tutorial'))

#7.fine the words with exactly 8 letters













  
      