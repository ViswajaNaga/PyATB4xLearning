# Hybrid inheritance - Mixture of Multiple and Hierarchical

# Multiple types of Inheritance such as single,multiple and multilevel Inheritance

class A: # father
    def methodA(self):
        return "Method A"

class B(A): # son1
    def methodB(self):
        return "Method B"

class C(A): # son2
    def methodC(self):
        return "Method C"

class D(B,C): # daughter--on rakshabandhan getting from bro1 and bro2 and she will get everything from father also
    # sister # Multiple, Multilevel- MRO(Method resolution order)-First
    def methodD(self):
        return "Method D"

d=D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())