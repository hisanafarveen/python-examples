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


