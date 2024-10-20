# Problem to find the maximum between three numbers

# logic building
# 3 inputs integers
# output is integer or string with max number

num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
num3 = int(input("enter number3"))

if num1 > num2 and num1 > num3:
    print("greater number is", num1)
elif num2 > num3 and num2 > num1:
    print("greater number is", num2)
else:
    print("greater number is", num3)


# OR

print(max(num1,num2,num3))
