# Static Methods
# A static method is a method that belongs to class
# rather than an instance of a class(object)

class MathOperation:

    def div(self,a,b):
        return a/b
    @staticmethod
    def add(a,b):
        return a+b

# Non static in nature. Object creation is mandatory
division=MathOperation()
print(division.div(6,3))

# static methods can be called directly without the object
print(MathOperation.add(5,2)) # we can use directly without creating object.Here self is also not required in the method