data=input("enter a value or 0 for quit")
while data!='0':
    if data=='8':
        data=input("enter a value 0 for quit")
        continue
    print(data)
    data=input("enter a value or 0 for quit") 
    
data=input("enter a value or 0 for quit")
while data!='0':
    if data=='10':
        data=input("enter a value 0 for quit")
        continue
    print(data)
    data=input("enter a value 0 for quit")

list3=[1,2,3,4,5,6,7,8,9,10]  
index=0
while index<len(list3):
    if index in [4,5,6]:
        index=index+1
        continue
    print(list3[index])
    index=index+1
    
list6=[11,12,13,14,15,16,17]
index=0
while index<len(list6):
    if index in[3,4]:
        index=index+1
        continue
    print(list6[index])
    index=index+1  
    
for value in range (0,101): 
    if(value%1==0) :
     print(value)

data=range(1,101) 
index=0
while index<len(data):
    if data[index]in range(50,61):
        index=index+1
        continue
    print(data[index]) 
    index+=1 
    
data=range(1,21)    
index=0
while index<len(data):
    if data[index]in range(10,16):
        index+=1
        continue
    print(data[index])
    index+=1
    
data=range(10,16)    
index=0
while index<len(data):  
    print(data[index])
    index+=1    
    
data=range(1,101)
index=0
while index<len(data):
    if data[index]in range(50,61):
        index+=1
        continue
    print(data[index])
    index+=1       

data=range(1,101)
index=0
while index<len(data):
    if data[index]in range(50,61):
        index+=1
        continue
    if data[index]==81:
        break
    print(data[index])
    index+=1       
        
        
    

    
