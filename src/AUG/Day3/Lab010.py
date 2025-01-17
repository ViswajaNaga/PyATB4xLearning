my_shopping_list = ["milk", "curd", "bread"]
my_marks = [90, 80, 70, 88]

# strings (str)
name = "viswaja"

print(type(name))
print(name.upper())
print(name.lower())
print(len(name))
print(name.capitalize())   # Viswaja
a = "90"
print(type(a))

b = 90
print(type(b))

name = "This is a line"
print(type(name))
# name=name+1  # Adding int to string is not possible (TypeError: can only concatenate str (not "int") to str)
name = name + "1"
name = name + str(2)
print(name)   # This is a line12

first_name = "naga"
last_name = "viswaja"
full_name = first_name + last_name  # concatenation
print(full_name)

# Concept of None
# Null is not present in python

How_many_planes_I_have = None
print(type(How_many_planes_I_have))  # NoneType

val = 0
print(type(val))  # int

# id- returns the identity of an object(address)

age = 10
a = 10

print(id(age))  # 140713012624088
print(id(a))  # 140713012624088
# to save the memory it will point to same container as value is same

a = 11
print(id(a))  # 140713012624120
