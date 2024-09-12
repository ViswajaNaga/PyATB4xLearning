# Method OverLoading---same name but work is different
# python does not support Method OverLoading in the traditional sense

# by default object is the father of every class even though we pass it or not.

class MathUtils(object): # IS A object - Single Inheritance

    def add(self,a,b):
        return a+b

    def add(self,a,b,c=0):
        return a+b+c

    def add(self,a,b,c=10,d=3):
        return a+b+c+d # 16 # latest one is used with additional default parameters

math=MathUtils()
op1=math.add(1,2) # TypeError: MathUtils.add() missing 1 required positional argument: 'c'
print(op1)  # 16(1+2+10+3)



