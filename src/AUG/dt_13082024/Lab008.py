# Take user inputs a,b and calculate sum,mul,div,sub

num1 = input("enter number1 ")
num2 = input("enter number2 ")

print(type(num1))
print(type(num2))

print("sum is ", num1 + num2)
"""
enter number1 6
enter number2 7
sum is 67----which is wrong. this is happening because type of input is always string so concatenation is happening
"""
# first we need to convert to int

num1 = int(input("enter number1 "))
num2 = int(input("enter number2 "))
print("sum is ", num1 + num2)
print("mul is ", num1 * num2)
print("div is ", num1 / num2)
print("sub is ", num1 - num2)

print(type(num1))
print(type(num2))
# whenever we divide there are high number of chance s of float like 3/2.
# as python is very smart language it considers as float for division

