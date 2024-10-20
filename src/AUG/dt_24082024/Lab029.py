def greet():
    print("hello, there")


def greet_by_name(x):  # here x can be anything it is just a variable name. x is called argument or parameter
    print("hello", x)


greet_by_name("viswaja")
greet_by_name(True)
greet_by_name(123)
greet_by_name(3.24)

# through user input
def greet(y):
    print("hello", y)


y = input("enter your name")
greet(y)
