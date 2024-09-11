# SINGLE Inheritance
class Parent:
    gold = "1kg"

    def home(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"

    def house(self):
        print("3BHK")

    def car(self):
        print("TATA Car")


child_obj = Child()
child_obj.home()
print(child_obj.gold)
child_obj.house()
child_obj.car()
print(child_obj.diamond)
print("====================================")
father_obj = Parent()
father_obj.home()
print(father_obj.gold)
