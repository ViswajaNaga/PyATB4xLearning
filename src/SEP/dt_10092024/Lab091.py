#two expected errors
a=int(input("enter number1")) # ValueError: invalid literal for int() with base 10: 'vish' if string is passed
b=int(input("enter number2"))
c=a/b # ZeroDivisionError: division by zero
print(c)


