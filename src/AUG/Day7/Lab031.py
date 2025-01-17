# create a program to find sum of 3 numbers from the user input

num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
num3 = int(input("enter number3"))


def sum_of_three_numbers(n1, n2, n3):
    return n1 + n2 + n3  ## when we want to store the value return is used.

result = sum_of_three_numbers(num1, num2, num3)
print(result)

result = sum_of_three_numbers(n1=num1, n2=num2, n3=num3)
print(result)


##################################

def sum_of_three_numbers(n1, n2, n3):
    print(n1 + n2 + n3)


result = sum_of_three_numbers(num1, num2, num3) # function is called
print(result) # no return type so None

result = sum_of_three_numbers(n1=num1, n2=num2, n3=num3) # function is called
print(result) # no return type so None

