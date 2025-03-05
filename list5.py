list8=["HISANA","PAVITHRA","parvathi","ihsan"]
smalllist8count=0
capitallist8count=0
for value in list8:
    if value.islower():
        smalllist8count=smalllist8count+1
    else:
        capitallist8count=capitallist8count+1
        
print("number of smalllist8 numbers:",smalllist8count)
print("number of capitallist8 numbers:",capitallist8count)        

data="e"
if data in ["a","e","i","o","u"]:
    print("vowelse")
else:
    print("not vowelse")    

list9=[1,4,6,7.6,9,"hisana",True,12-12j]
for index in range(len(list9)):
    print(list9[index])

index=0
while index<len(list9):
    print(list9[index])
    index=index+1
    
list8=["HISANA","PAVITHRA","parvathi","ihsan","false",4-8j]
for index in range(len(list8)):
    print(list8[index])
 
index=0
while index<len(list8):
    print(list8[index])  
    index=index+1
index=len(list8)-1
while index>=0:
    print(list8[index])  
    index=index-1  
list2=["farwa",7,9,6,24,"FATHIMA",7-3J,True,"muhammed"]   
index=8
while index>-1:
    print(list2[index])
    index=index-1 
    
index=len(list2)-1 
while index>=0:
    print(list2[index])
    index=index-1
index=0
while index<len(list2):
    print(list2[index])
    index=index+1 

for row in range(0,6):
     for col in range(0,row):
         print("*",end="")  
     print("")       
 
row=0
while row<6:
    col=0
    while col<row:
        print("*",end="")
        col=col+1
    print("")
    row=row+1    
    
for row in range(6,0,-1):
     for col in range(0,row):
        print("*",end="") 
     print("")   
     
row=6
while row>0:
    col=0
    while col<row:
        print("*",end="")
        col=col+1
    print("")
    row=row-1
    
for row in range(8,0,-1):
    for col in range(0,row): 
         print(col,end=" ")
    print("")   
    
row=8
while row>0:
    col=0
    while col<row:
        print(col,end=" ")
        col=col+1
    print("")             
    row=row-1
for row in range(0,7):
    for col in range(0,row):
         print(col,end=" ")
    print("")  
  
row=0
while row<7:
    col=0
    while col<row:
        print(col,end=" ")
        col=col+1
    print("")
    row=row+1    
for row in range(8,0,-1):
    for col in range(2,row):
        print(col,end=" ")
    print("")    
    
row=8
while row>0:
    col=0
    while col<row:
        print(col,end=" ")
        col=col+1

data=input("enter a value or 0 for quit")
while data!='0':
    print(data)
    data=input("enter a value or 0 for quit")

data=input("enter a value or q for quit")
sum=0
while data!='q':
    sum=sum+int(data)
    print(sum)
    data=input("enter a value or q for quit")
sum  
data=input("enter a value or q for quit")
sum=0
while data!='q':
    print(data)
    sum=sum+int(data)
    data=input("enter a value or q for quit")
sum

data=input("enter a value or z for quit")
sum
  
  