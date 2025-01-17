# when we assign the variable in the class it becomes hardcoded value

class Person:
    name = "None"

    def walk(self, name):
        self.name = name
        print(self.name)


lucky = Person()
lucky.walk("lucky")

chinnu = Person()
chinnu.walk("chinnu")

print("===============================================================")


# when we assign the variable in the class it becomes hardcoded value

class Person:
    name = "Amit"  # hardcoded value. common across all variables

    def walk(self, name):
        self.name = name
        print(self.name)


luckyobj = Person()
print(luckyobj.name)

chinnuobj = Person()
print(chinnuobj.name)

print("===============================================================")

class Person:

    def __init__(self,name):
        self.name=name
# constructor is basically used to change the value of Instance variable
    def walk(self):
        print(self.name)

luckyobj = Person("lucky")
print(luckyobj.name)

chinnuobj = Person("chinnu")
print(chinnuobj.name)