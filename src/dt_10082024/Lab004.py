#  Keywords and Identifiers
#  Keywords are also called Reserved words meaning a pen cannot be called with a different name
#  a pen cannot be called as a book and a book cannot be called as a pen, a specific name is already reserved for them.

import keyword

print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# variables are basically like containers that stores the value

age = 20
print(age)
print(type(age))

age = "ravi"  # variable name = Variable Value
print(age)
print(type(age))
