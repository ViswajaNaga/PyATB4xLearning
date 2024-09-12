# OOPS
# Class- Blue print
# Object- Instance of class
# Encapsulation-private__, protected_,public --> Hiding my own methods and Variables
# Inheritance --> single, multiple, multilevel, hybrid, Hierarchical
# Polymorphism--> Method Overriding, Method Overloading(not applicable in python)
# Method Overriding - between one or more classes
# Method Overloading - Within the class
# self, super,__init__

# Abstraction - Hide the details and show what is required.--> Hiding Classes.

# car - wit key __private, tyres-public
# car - multiple classes --> engine, gearbox
# car - driver --> engine, gearbox? --> not interested

from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def sound(self):
        pass#TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'sound'
# as the method sound is incomplete in nature in Animal class, somebody has to complete it in different class
class Dog(Animal):
    pass
    # def sound(self):
    #     print(self.name,"Barks")

d=Dog("Bittu")
d.sound()








