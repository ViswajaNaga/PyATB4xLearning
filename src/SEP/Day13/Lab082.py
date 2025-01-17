# Method OverLoading---same name but work is different(means addition of 2 numbers or addition of 3 numbers)
# python does not support Method OverLoading in the traditional sense
# Method Overloading-- same method name created within the class with different arguments
# method overloading is the concept in the class we can have same name with different arguments but overall in python it is not supported

# by default object is the father of every class even though we pass it or not.

class MathUtils(object): # IS A object - Single Inheritance
# method overloading not supported
    def add(self,a,b):
        return a+b

    def add(self,a,b,c=0): # method overloading is supported only if we give default value
        return a+b+c

    def add(self,a,b,c=10,d=3):
        return a+b+c+d # 16 # latest one is used with additional default parameters

math=MathUtils()
op1=math.add(1,2) # TypeError: MathUtils.add() missing 1 required positional argument: 'c'-- if default value is not provided
print(op1)  # 16(1+2+10+3)



