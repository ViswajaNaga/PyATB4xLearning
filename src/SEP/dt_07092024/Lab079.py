class Shape:
    def area(self):
        print("Area of shape is")

class Rectangle:
    def area(self,length,width):
        self.length=length
        self.width=width
        return self.length*self.width

class Circle:

    def area(self,radius):
        self.radius=radius
        print(3.14*self.radius*self.radius)

shape1=Rectangle()
print(shape1.area(3,4))

shape2=Circle()
shape2.area(10)