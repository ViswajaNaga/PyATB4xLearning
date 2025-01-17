# try , except and Finally

try:
    a = int(input("enter number1"))
    b = int(input("enter number2"))
    result = a / b
except ValueError as VE:
    print("Value error, you have entered string instead of int")

except ZeroDivisionError as ZDE:
    print("ZeroDivisionError,Don't use b value as zero")

else:
    print(result)

finally:
    print("this code will be always executed")