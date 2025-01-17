class Grandparent:
    key_gold="1kg"
    def gp_method(self):
        return "Grandparent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "parent's method"

class child(Parent):
    def child_method(self):
        return "Child's method"

c=child()
print(c.gp_method())