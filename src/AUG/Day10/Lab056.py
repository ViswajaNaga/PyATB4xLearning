# Class and Object Assignment
#
# Create an Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, print_details,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self,eid,name,age,phone,address):
        self.eid = eid
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def walk(self):
        print("I am walking", self.name )
    def talk(self,name):
        print("I am talking", name)


e1=Employee(1,"ram",30,4564564567,"hyd")
print(e1.eid)
print(e1.name)
print(e1.age)
print(e1.phone)
print(e1.address)
e1.talk('myself')
e1.walk()

eid=int(input("enter ur id: "))
name=input("enter ur name: ")
age=int(input("enter ur age: "))
phone=int(input("enter ur phone: "))
address=input("enter ur address: ")

e2=Employee(eid,name,age,phone,address)

print(e2.eid)
print(e2.name)
print(e2.age)
print(e2.phone)
print(e2.address)
e2.talk("yourself")
e2.walk()



