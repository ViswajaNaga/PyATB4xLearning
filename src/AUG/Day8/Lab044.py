import math


def power_of_num(n):
    return math.pow(n,2)

op=power_of_num(10)
print(op)

op2= lambda n : math.pow(n,2)
print(op2(3))

op3= lambda  : math.pow(int(input("enter the number\n")),2)
print(op3())

#__init__.py

# create dir - normal folder - python doesn't search the files here or code here.

# package is a folder with file __int__.py - python will search the code here
# __init__.py -> dir -> module (where python will search better)