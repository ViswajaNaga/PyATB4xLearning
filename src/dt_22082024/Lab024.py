# CONTINUE statement

# CONTINUE statement skips the current iteration of the loop and moves to next iteration.

for number in range(10):
    if number%2==0:
        continue   # skip
    print(number)


for number in range(10):
    if number%2==0:
        pass   # skip
    else:
        print(number)

# | i  | Condition | O/P
# | 0  | 0%2 == 0 -> True | continue - skip No O/P
# | 1  | 1%2 == 0 -> False | 1
# | 2  | 1%2 == 0 -> True | continue - skip No O/P
# | 3  | 3%2 == 0 -> False | 3


# pass - can be used in the statement, functions, class and objects
# Continue can be used only in statements and cannot be used in functions, class and objects
