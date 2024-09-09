class Calc:

    def __init__(self, a, b):
        print("parameterised Constructor")
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object1 = Calc(3, 4)
object2 = Calc(8, 10)

output_sum = object1.sum()
output_sub = object2.sub()

print(output_sum)
print(output_sub)

