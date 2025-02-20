hg='remesh'
hg
id(hg)
type(hg)
hg[:3]
hg[-1]
hg[4]
j=None
j
type(j)
hg[::-1]
hg[::2]
hg[1::2]
tuple1=567,457.898,-3467,12-56j,3456,"a",True
type(tuple1)
dir(tuple1)
tuple1.count(567)
tuple1.index("a")
tuple1[3]
tuple1=4567,3456.456789,-456321,122-12j,"fathima",False
type(tuple1)
dir(tuple1)
tuple1.count(4567)
tuple1.index("fathima")
tuple1[5]
tuple1[-2]
tuple1[3]
list1=[234,12345.678,-67898,23-15,"sujatha",True]
list1
type(list1)
dir(list)
list1.count(123)
list1.count(234)
list1.index("sujatha")
list1[4]
list1[-3]
list1[-1]
list1[:1]
list1.append(56)
list1.append(34)
list1.insert(1,45)
list1.insert(2,18)
list1.append(99)
list1.insert(6,1000)
list1.append(20000)
list1[6]
list1[-5]
list1[-1]
list1[-4]
list1[9]
list1.append(tuple1)
list1.extend(tuple1)
list1
tuple4=[10500,28000.40,-14567,62-38J,"hana",False]
tuple4.append(14)
tuple4.insert(3,4500)
tuple4
tuple4.append(list1)
tuple4.extend(list1)
tuple4
list4=[1234567,23.567,-34567,"riza",True]
list4.pop(-1)
list4.remove(1234567)
list4
tuple7=[4500,6750.450,123-34,"rahul",False]
tuple7.pop(-3)
tuple7.remove(4500)
tuple7
list1=["hisana","safa","fazlu","muhammed","ihsan","rahmathuneesa"]
list2=[123,15070,5050,20000,400,8540,45678]
list1.sort()
list1.sort(reverse=True)
list1
list2.sort()
list2.sort(reverse=True)
list2
list1.reverse()
list1
list6=list1
list7=list1.copy()
list1
list6
list7
id(list1)
id(list7)
id(list6)
list6
set1={'safa','hisana','muhammed','safa','ihsan','rahmathuneesa'}
set1
id(set1)
type(set1)
dir(set1)
set2={124,156,168,887,1000,5800,4090,2345,654,8765}
set3={144,230,124,1000,111,3313,333,2345,654,8097}
set2.intersection(set3)
set2.difference(set3)
set3.difference(set2)
set2.symmetric_difference(set3)
set2.update(set3)
set2
set5={1890,4679,2479,1236,2400}
set8={3300,2300,1599,3980,844}
set2.isdisjoint(set3)
set10={2,3,4,5,6}
set11={2,3,4,5,6,7,8,9,10}
set10.issubset(set11)
set11.issuperset(set10)

dict1={"name":"Pradeep","age":24,"place":"tirur"}
dict1["age"]
dict1["name"]
type(dict1)
dir(dict1)
dict3={"name":"hisana","age":23,"place":"vettathur"}
dict3["name"]
dict3["place"]
dict3["age"]
type(dict3)
dir(dict3)
dict7={"name":"rama","age":28,"gender":"female"}
dict7["gender"]
dict7["age"]
dict5={"name":"sana","age":20,"place":"melattur"}
dict5["place"]
dict5["age"]
dict5.keys()
dict5.values()
dict5.items()
dict5['state']="kerala"
dict5['dst']="pkd"
dict5.update({"state":"Kerala","dst":"mpm"})
dict5
dict9={"name":"muhammed","age":49,"place":"thiruvizhzmkunnu"}
dict9.keys()
dict9.values()
dict9['state']="kerala"
dict9["dst"]="kozikkod"
dict9.update({"state":"Thamiznadu","dst":"palakkad"})
dict9

age=34
print("my age is",age)
print(f"my age is {age}")
print("I'm going to inject %5.6f here." %12)
print("my age is",25)
print(f"my age is{25}")
print("Iam going to inject %3.10f here. "%12)
a ="hisana"
b ="safa"
print("hello my name is %r \n %r"%(a,b))
print("Iam going to inject %s text here,and %stest here." % ( 'some','more'))           
a=1
a
print(13)
print("Iam going to inject %10.4f here. "%12)                           
print('this is a string with an {1} {1}'. format("insert","hello"))
a=12
b=24
print('this is a string with an {a} {b}'. format(a=23,b=56))

print('this is a string with an {0:#^8} {1:#^8}'. format("insert","hello"))
print('this is a string with an {0:*>8} {1:*>8}'. format(1000000,2000))
print(f"hello{age:.4f}")
age=40
print("my age is",age)
print(f"my age is{age}")
print("my age is",24)
print(f"my age is{24}")
print ("Iam going to inject %7.4f here."%12)
print("Iam going to inject %5.8f here."%15)
a="sana"
b="suhana"
print("hello my name is %r \n %r"%(a,b))

print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apples', 3.))
print('{0:8} | {1:8}'.format('Oranges', 10))
print('{0:<8} | {1:8}'.format(1000,2))
print('{0:3} |{1:5}'.format(3000,9))
c=10
d=20
print('this is a string with an {c} {d}'. format(c=10,d=20))
print('this is a string with an {0:#^8} {1:#^}')
