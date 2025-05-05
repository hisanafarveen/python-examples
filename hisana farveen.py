import re
pattern=r'^this.*python$'
print(re.search(pattern,'This tutorial is about python'))
pattern
pattern=('[a-r]')
print(re.search(pattern,"my name is hisana"))

pattern=r'^78er/8*$'
print(re.search(pattern,'0088ert'))

import re
regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za\d]{8}$"
def check_password(p):
    if re.search(regex,p):
        print('success')
    else:
        print('no')
check_password('*ASwe.2AEqa34')  


import re
regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
def check_email(email):
    if re.search(regex,email):
        print('success')
    else:
        print('no')
check_email('resha@gmail.com')   

import re
regex=r'^(9{1})(\d{9})$'
def check_phone(phoneno):
    if re.search(regex,phoneno):
        print('success')
    else:
        print('no') 
check_phone('9523755569')      


class Data_Analytics:
    def __init__(self,name1, name2):
        self.name1=name1
        self.name2=name2

    def hisana1(self):
        return (self.name1, "can talk")

    def hisana2(self):
        return (self.name2, "can walk")

hisana_f=Data_Analytics("hisana","kk")
dir(hisana_f)
hisana_f.name1
hisana_f.name2
hisana_f.hisana1()
hisana_f.hisana2()
yahiya_m=Data_Analytics("yahiya","vk")
yahiya_m.hisana2()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person()
print (p1)      
class student:
    def  __init__(self,name,ids):
        self.name=name
        self.id=ids
    def  print_name(self):
        print(f"name:{self.name}")
    def print_id(self):
        print(f'id:{self.id}')

st1=student('anu',1)
st1.name
st1.id
st1.print_name()
st1.print_id()
import re
st2=student("ravi",4)
st2.print_name()

class student:
    def __init___(self):
        self.name=input("enter name:")
        self.id=input("enter id:")
    def print_name_(self):
        print(f"name:{self.name}")
    def print_id(self):
        print(f"id:{self.id}")

st1=student() 
st1.print_name()          

class account:
    def __init__(self,accnt_num,accnt_blnce):
        self.accnt=accnt_num
        self.balance=accnt_blnce
    def withdraw(self,amount):
        if self.balance-amount>=0:
            print("you can withdraw the ampunt") 
            self.balance=self.balance-amount
        else:
            print("withdrawal failed") 
    def display(self):
        print(self.accnt,"your blance is", self.balance)   

accnt1=account(12334435,10000)
accnt1.withdraw(50004)   

accnt1.display()

class animal:
    def __init__(self):
        self.name=input("enter name:dog")
        self.color=input('color:black')
    def walk(self):  
        print("animal can walk") 
a1=animal()
print(a1.name) 
a1.walk()

class book:
    def __init__(self):
        self.name=input("enter name:hisana")
        self.id=input("enter id:123")
    def 















        self.name=input("book name:the alchemist")
        self.rate=input("book rate:400")
        self.purchased=input("book purchased= edumart")
    def    





    