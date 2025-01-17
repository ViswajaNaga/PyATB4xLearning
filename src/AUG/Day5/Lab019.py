# Problem to find the maximum between two numbers

# logic building
# user inputs = 2 integers(ask from interviewer if datatype is int or float that is required)
# output--> integer whichever is greater
# input method

num1 = int(input("enter number1"))
num2 = int(input("enter number2"))

if num1>num2:
    print("max is", num1)
else:
    print(f"{num2} is max")