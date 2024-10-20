# PyATB Students
# Attributes /Properties /Data members
# Behaviour /Methods / member functions

# Attributes-name, id, email,phone_no, address,gender,city,location
# by which u recognize

# Behaviour- talk,walk,write,sing,dance,watch,listen,smile,sleep,cry
# you can do something

class Person:
    # Attributes
    id=None
    name=None
    age=None
    email=None
    height=None
    gender=None
    phone_no=None
    address=None

# behaviour/Methods
# self will be the first argument in every behaviour
    def talk(self): # No Argument with No Returntype
        print("I can talk")

    def sleep(self,name): # Argument with No Return
        print("I sleep more", name)

    def laugh(self,name): # Argument with Return
        print("I laugh less", name)
        return None

    def walk(self): # No Argument with return
        return "I walk slow"

# create an object of class
# Object Reference = ClassName() -> object

ram=Person()
ram.name="RAM"
print(ram.name)
ram.talk()

sita=Person()
sita.name="SITA"
print(sita.name)
sita.talk()
