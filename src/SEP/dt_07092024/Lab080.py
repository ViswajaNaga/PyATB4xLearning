# Polymorphism
# method Overriding

class Shape:
    def area(self):
        print("Area of shape is")

class Rectangle(Shape): # IS A Single Inheritance

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):  # local has more preference
        return self.length*self.width

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(3.14*self.radius*self.radius)

shape1=Rectangle(3,4)
print(shape1.area())

shape2=Circle(10)
shape2.area()