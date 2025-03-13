def demo3(num):
    for value in range(0,num):
        if value%2==0:
            print(value)
                        
demo3(200) 

def demo6(num):
    for row in range(0,num):
        for col in range(0,row):
          print(col,end=" ")
        print("")    

demo6(10)

def demo6():
    list9=[]
    for value in range(0,101):
        if (value%3==0)|(value%5==0):
            list9.append(value)
    return list9
    
         
b=demo6()
b

def demo8():
    data=input("enter a value or 0for quit")
    while data!="0":
        if data=='10':
            data=input("enter a value or 0for quit")
            continue
        print(data)
        data=input("enter a value or 0 for quit")
        
demo8()

def demo4():
    row=6
    while row>0:
        col=0
        while col<row:
            print("*",end="")
            col=col+1
        print("")
        row=row-1
    
demo4()

a=int(input("enter a value "))
b=int(input("enter a value "))
c=int(input("enter a value "))
if a==b==c:
    print(3*a)
else:
    print(a+b+c)
    
data="o"
if data in ["a","e","i","o","u"]:
    print("voweles")
else:
    print("not voweles")
    
a=int(input("enter a value for 0 in quit"))
b=int(input("enter a value for 0 in quit"))
c=int(input("enter a value for 0 in quit"))
if (a==b) and (a==c):
    print("sum=0")
elif (b==a)and (b==c):
    print("sum=0")
else:
    print("sum=",a+b+c)
    
    
    
        
        
        
        
    






