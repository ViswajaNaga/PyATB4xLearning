print("-----start of program-----")
try:
    a=int(input("enter number1")) # ValueError: invalid literal for int() with base 10: 'vish' if string is passed
    b=int(input("enter number2"))
    c=a/b # ZeroDivisionError: division by zero
    print(c)
except Exception as e: # Exception is a class in Builtin which contains all types of exceptions.
    print(e)
    print("please check your inputs, it shouldn't be a string or zero")

print("-----end of program-----")

# try:
#     try this code, if error
# except:
#     execute me if try has some error
