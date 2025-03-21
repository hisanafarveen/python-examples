list1=[10,12,15,17]
result=sum(list1)
result
print(result)
sum=0
for value in list1:
    sum=sum+value
sum     
   
list2=[11,123,27,105]
max=list2[0]
for value in list2:
    if max<value:
        max=value
    else:
        pass
print(max)

sum=0
for value in list1:
    sum=sum*value
sum  

list3=[1,5,7,9,1,"hisana",-1,"safa"]
set(list3)
list5 =[]
len(list5)
list4=["yahiya",4,5,7,8,123,-33,"fathima"]
list5=list4
list6=list4.copy()
list6

list11={2,4,6,8,10,-5}
list12={1,2,3,4,5,-3}
list11.intersection(list12)

list8=[1,3,6,1,7,9,3,6,12,15,18,6]
list9=[]
for value in list8:
    if value not in list9:
        list9.append(value)
list9  
list10=list(set(list8))   
list10  
list22=[5,10,40,50,70,100]
for index in range(0,len(list22)):
    print(index,list22[index])
    
list21=['abc','xyn','aba','1221']
for value in list21:
    if value[0]==value[-1]:
        print(value)
list5=[]
for value in range(1,31):
    list5.append(value**2)
    if value<6 or value>25:
        print(value,value**2)
list5        

def sum1(a=0,b=0):
    return a+b

sum1(12,34)

def sum2(*args):
    print(args)
    return sum(args)
sum2(12,23,67,89)


def sum2(*args):
    print(args)
    sum=0
    for value in args:
        sum=sum+value
    return sum

sum2(12,23,12,78)

def sum4(*args):
    print(args)
    return sum(args)
sum4(34,67,80,23)

list5=[]
list6=["HISANA","SAFA","SANA","muhammed"]
for value in list6:
    if value.islower():
        print(value)
             
    

tuple6=("HISANA","SAFA","SANA","muhammed")
def lowercase(*tuple6):
    for value in tuple6:
        if value.isupper():
            print(value)


lowercase("HISANA","SAFA","SANA","muhammed","PRADEEP")

def sum4(*isupper):
    print(isupper)
    return sum(isupper)
sum4(tuple6)

list12=["yahiya","MANU","febina","SAFNA"]

def lowercase(*list12):
    upperlist=[]
    lowerlist=[]
    for value in list12:
        if value.isupper():
            upperlist.append(value)
        else:
            lowerlist.append(value) 
    return upperlist,lowerlist
             
lowercase("yahiya","MANU","febina","SAFNA")

l10=[45,-2,458,64,5,-1,0.11,47.8,47.3]
def  largest(abc):
    max=1
    for value in abc:
        if value>max:
            max=value
        else:
            pass
    print(max) 
largest(l10)    
l10=[45,-2,458,64,5,-1,0.11,47.8,47.3]
def smallest(abc):
    min=-1
    for value in abc:
        if value<min:
            min=value
        else:
            pass
    print(min)
smallest(l10)
  
l10=[45,-2,458,64,5,-1,0.11,47.8,47.3]   
def count(abc):
    count=0
    for value in abc:
            if value >-1000:
                count=count+1
    print(count)            
count(l10)   


l10=[45,-2,458,64,5,-1,0.11,47.8,47.3]
even=0
odd=0
for value in l10:
    if value%2==0:
        even+=1
    else:
        odd+=1    
print (" even number",even)
print("odd number",odd)  

        

          
                
                
                
    

         