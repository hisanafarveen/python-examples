a="1234abcd"
rev=a[::-1]
print(rev)

def sum(*args):
    print(*args)
    sum=0
    for value in args:
        sum=sum+value
    return sum
sum(8,2,3,0,7) 

b=[6,7,8,9,10]
def multiply(*args):
    print(*args)
    result=1
    for value in args:
        result=result*value
    return result    
multiply(b)



def sum(*list1):
    print(list1)
    result=0 
    for value in list1:
        result=result+value
        return result
    
sum(123,234,678)


def sum (*list5):
    print(list5)
    for value in list5:
        if value.isupper(): 
             print(value)
        
sum("hisana","safa","sana","SHAMNA","YAHIYA","pradeep")

def sum(*args):
    print(args)
    for value in args:
        if value.islower():
            print(value)
sum("hisana","safa","sana","SHAMNA","YAHIYA","pradeep")

def info(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,":",v)        

info(name="Pradeep",place="Tirur",Eng=23,Sanskrit=35,maths=36)
info(name="Hisana",place="PMNA",Eng=23,Arabic=35,maths=36,Hindi=45)
info(name="safa",place="malappuram",arabic=40,eng=44,hindi=31)

list6=[10,5,7,8,9,2]
list5=[]
for value in list6:
    list5.append(value**2)
    
list5
def square(value):
    return value**2

list(map(square,list6))

list(map(lambda value:value**2,list6))

list10=["hisana","safa","yahiya","femina"]
list11=[]
for value in list10:
    list11.append(value.upper())
list11
def upper(value):
    return value.upper()

list(map(upper,list10))
     
list(map(lambda value:value.upper(),list10))    

for value in list10:
    print(value[:3])
    
list10[:3]
def demo():
     for value in list10:
       print(value[:3])
demo(list10) 

list10=["hisana","safa","yahiya","femina"] 
def prin(value):
    return value[:3]    
list(map(prin,list10))
list(map(lambda a:a[:3],list10))
