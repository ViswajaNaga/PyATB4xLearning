# Encapsulation
# protects its variables by using methods is called encapsulation
# Hides the data members( class variables, Instance variables)
# by using only methods
# there are 3 types of variables-public, private and protected

class Car:
    model=None
    name=None
    password=123

    def __init__(self):
        print("DC")


    def change_password(self):
        self.password="vishwa"

obj_ref=Car()
print(obj_ref.password)
obj_ref.change_password()

print("==============================================")

class Car:
    model=None
    name=None
    password=123

    def __init__(self):
        self.password = "vishwa"

    def change_password(self):
        print(self.password)

obj_ref=Car()
print(obj_ref.password)
obj_ref.change_password()


