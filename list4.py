list15=[123,345.78,1500,60.90]
tuple1=tuple(list15)
tuple1
p=90
bin(p)
oct(p)
hex(p)
hex(95)
chr(65)
ord('}')
list14=[567,9.9087,7654]
tuple5=tuple(list14)
tuple5
z=750
bin(z)
oct(z)
hex(z)
chr(z)
ord("h")
ord('5')
5<7
7>=7
7!=6
a=7
a+=7
a-=7
a
a=a+7
a+=7
5678 not in list14
a=89
88 is a
10<5
7>4
10!=8
b=10
b-=10
b+=10
b
b=b-10
list7=[234,56,89]
56 not in list7
100 is list7
89 is list7
4 not in list7
70 not in list7
list40=[1080,'ravi',13.68,78] 
tuple8=(1236,456,309,33)
dic3={"name ": "hisana", "age":32 ,"location" : "perinthalmanna"}
print(list40[0])
print(list40[1])
print(list40[2])
for value in list40:
    print(value)  
    
for valu in tuple8:
    print(valu)
    
for k,v in dic3.items():
    print(k,":",v)

list(range(1,10))
for index in range(0,3):
    print(list40[index])
    
for index in range(0,len(list40)):
    print(list40[index])
for index in range(0,len(tuple8)):
    print(tuple8[index])

for value in range(0,101,2):
    print(value)
for value in range(0,101):
    if value%2==0:
        print(value)



    if valu%2==1:
        print(valu)
list7=["sana","safa","rama","rana","pavithra"]
for value in list7:
    if len(value)>4:
        print(value)

list9=["RESHMA","Ramyaremesh","PARVATHY",'78']
for value in list9:
    if value.isnumeric():
        print(value)
        
list21=["HISANA","suhana","IHSAN",'145','47',"Fahmida"]  
for value in list21:
     if value.isalpha():
         print (value)
list44=["farsana","SUHADA","Farhana","56"]  
      
for value in range(0,101):
    if (value%3==0)|(value%5==0):
        print (value)

for value in range (500,1501):
    if (value%5==0)&(value%7==0):
        print(value)
        
for value in range (1000,3000):
    if (value%5==0)&(value%3==0):
        print(value)
   
for value in list5:
    result=result+value
    
result

list6=[12,45,78,90,14,50]
result=1
for value in list6:
    result=result*value   
result
list90=[]
for value in range(0,101):
    if (value%3==0)|(value%5==0):
        list90.append(value)

list90
list9=[]
for value in range(0,101):
    if (value%3==0)|(value%5==0):
        list9.append(value)
        
list9 
list12=[50,81,56,89,90,]
oddlist=[]
evenlist=[]
for value in range(50,91):
    if value%2==0:
        evenlist.append(value)
    else:
        oddlist.append(value)
evenlist
list21=["HISANA","suhana","IHSAN",'145','47',"fahmida"]
upperlist=[]
lowerlist=[]
otherslist=[]
for value in list21:
    if value.isupper():
        upperlist.append(value)
    elif value.islower():
        lowerlist.append(value)
    else:
        otherslist.append(value)
upperlist
lowerlist
otherslist
list43=["hana",'67','809','789',"FARSANA","nifsa","PAVITHRA","@@@]"]
upperlist=[]
lowerlist=[]
otherslist=[]
for value in list43:
    if value.isupper():
        upperlist.append(value)
    elif value.islower():  
        lowerlist.append(value)
    else:
        otherslist.append(value)
otherslist          

"*"*5
"*"*1
"*"*2
"*"*3

for value in range(1,3):
    print("*"*value)

for value in range(5,0,-1):
    print(" ? "*value)

for row in range(1,6):
    for col in range(0,row):
        print("*",end="")
    print("")

for row in range(1,6):
    for col in range(0,row):
        print(row,end="")
    print("")
for row in range(1,6):
    for col in range(1,row):
        print(col,end="")
    print("")

for row in range(5,0,-1):
    for col in range(0,row):
        print(row,end="")
    print("") 
for row in range(1,6):  
    for col in range(5,row-1,-1):
        print(row,end="")
    print("") 
     
for row in range(0,10):
    for col in range(6,row-1,-1):
        print(row,end="")
    print("") 
list1=range(1,11) 
index=0  
for row in range(1,5):
    for col in range(0,row):
        print(list1[index],end=" ")
        index=index+1
    print("")
list2=range(10,25)
index=0
for row in range(1,6):
    for col in range(0,row):
        print (list2[index],end=" ")
        index=index+1
    print("")   
    
     
for row in range(1,6):
    for col in range(6,row-1,-1):
        print(" ",end=" ")
    for col in range(1,row+1):
        print(col,end=" ")
    print("") 
    
for row in range (1,6):
    for col in range(6,row-1,):
        print(" ",end=" ") 
    for col in range (1,row+1):
        print(col,end=" ")
    print("")           
for row in range (1,6):
    for col in range (5,row,-1):
        print (" ",end=" ")
    for col in range (1,row+1):
        print(col,end=" ")
    print("")   
for row in range (5,0,-1):
    for col in range(row,0,-1):
        print(col,end=" ")
    print("")      
for row in range(1,10):
    for col in range(1,row+1):
        print(col*row,end=" ")
    print("")
for row in range (8,1,-1):
    for col in range(8,row,-1):
        print(" ", end='') 
    for col in range(1,row,+1):
        print("*", end=' ') 
    print("")  
    
for row in range (1,6):
    for col in range(0,row):
        print("*",end=" ")
    print("")
else:    
    for row in range (6,0,-1):
        for col in range(0,row):
            print("*",end=" ")
        print("")  
        
        
for row in range (1,7):
    for col in range(0,row):
        print("*",end=" ")
    print("")
else:   
    print("")  
    for row in range (6,0,-1):
        for col in range(0,row):
            print("*",end=" ")
        print("")
for row in range(6,1,-1):
    for col in range(7,row,-1):
        print(" ",end='')
    for col in range(1,row):
        print("*",end=' ')
    print("")        
for row in range(1,7):
        for col in range(6,row,-1):
            print(" ",end='')
        for col in range(1,row+1):
             print("*",end=' ')
        print("") 
for row in range(1,7):
        for col in range(6,row,-1):
            print(" ",end='')
        for col in range(1,row+1):
             print("*",end=' ')
        print("")
for row in range(6,1,-1):
    for col in range(6,row-1,-1):
        print(" ",end='')
    for col in range(1,row):
        print("*",end=' ') 
    print("")                   
data=65                                      
for row in range(8,0,-1):
    for col in range(0,row,+1):
        print(chr(data),end=" ")
        data=data+1
    print("") 
list2="python" 
for row in range(0,len(list2)):
    for col  in range(0,row+1):
        print(list2[col],end="")
    print("")
        
list6="hisana"   
for row in range (0,len(list6)):
    for col in range(0,row+1):
        print(list6[col],end="")
    print("") 
  
    