# User Defined
# 1.They can't return -> non return
# 2.They can return something
# They have parameters
# They don't parameters / arguments


# 1. No Return Type and No Parameter / Argument - NRNP
def greet():
    print("hello world")

result=greet()
print(result)


# 2. No Return Type and with Argument
def greet_by_name(name):
    print("hello",name)

result=greet_by_name("vish")
print(result)

# 3. No Return Type with default argument.
def greet_with_default_argument(name="everyone"):
    print("hello", name)
    print("hello", name.upper())

greet_with_default_argument("heyansh")
greet_with_default_argument()
greet_with_default_argument(name="Hruthvik") # this is called positional argument

def multiple_args(name1="john", name2="joy", name3="ice"):
    print("multiple args", name1, name2, name3)

multiple_args("ram","sita","ravi")
multiple_args()

# 4. Return Type with Argument

def sum_of_two_num(num1,num2):
    return num1+num2

# result=sum_of_two_num(2,3)
result=sum_of_two_num(num2=10,num1=20)

print(result)