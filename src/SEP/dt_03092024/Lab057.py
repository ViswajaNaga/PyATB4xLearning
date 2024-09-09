# Take input and create a class in python


class Person:

    def __init__(self):
        self.eid = int(input("enter ur eid "))
        self.name = input("enter ur name ")
        self.age = int(input("enter ur age "))
        self.phone = int(input("enter ur phone "))
        self.address = input("enter ur address ")

    def display_information(self):
        print(f"eid is {self.eid}")
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"phone is {self.phone}")
        print(f"address is {self.address}")
        print(f"eid is {self.eid}", f"name is {self.name}", f"age is {self.age}", f"phone is {self.phone}",
              f"address is {self.address}")


# create an object
person1 = Person()

# call the function
person1.display_information()
