# Static Methods
# A static method is a method that belongs to class
# rather than an instance of a class(object)

class MathOperation:

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def add(a, b):  # static doesn't belong to object, it belongs to class...so self is not required
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


# Nonstatic in nature. Object creation is mandatory
object_ref = MathOperation()
print(object_ref.div(6, 3))
print(object_ref.mul(6, 3))
# static methods can be called directly without the object
print(MathOperation.add(5, 2))  # we can use directly without creating object.
print(MathOperation.sub(5, 2))
# Here self is also not required in the method
