class Calc:

    def __init__(self):
        print("Default Constructor")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object = Calc()
output_sum = object.sum(4, 6)
output_sub = object.sub(4, 6)
output_mul = object.mul(4, 6)
output_div = object.div(4, 6)

print(output_sum, output_sub, output_mul, output_div)

##########################

a = int(input("enter the value of a"))
b = int(input("enter the value of b"))

output_sum = object.sum(a, b)
output_sub = object.sub(a, b)
output_mul = object.mul(a, b)
output_div = object.div(a, b)

print(output_sum, output_sub, output_mul, output_div)
