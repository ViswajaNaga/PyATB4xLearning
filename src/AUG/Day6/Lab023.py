# While loop
# syntax

# variable_name=0
# while condition:
#     execute this code
#     variable_name increment

i=0
while i<10:
    print(i, end=" ")
    i=i+1   # in python we don't have i++ or i--. It is only in java

# BREAK
for i in range(0,10):
    print(i)
    if i==5:
        break   # going out of the loop

mylist=list(range(10))    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  start and step are optional in range, by default it will take 0 as start
print(mylist)


for i in range(0,10):
    if i==5:
        print(i)
    else:
        print("no o/p")

# | i  | Condition | O/P
# | 0  | 0 == 6 -> False | O/P -> No O/P
# | 1  | 1 == 6 -> False | O/P -> No O/P
# | 2  | 2 == 6 -> False | O/P -> No O/P
# | 3  | 3 == 6 -> False | O/P -> No O/P
# | 4  | 4 == 6 -> False | O/P -> No O/P
# | 5  | 5 == 6 -> False | O/P -> No O/P
# | 6  | 5 == 6 -> True | O/P -> 6
# | 7  | 7 == 6 -> False | O/P -> No O/P
# | 8  | 8 == 6 -> False | O/P -> No O/P
# | 9  | 9 == 6 -> False | O/P -> No O/P

for i in range(0,10):
    if i==5 or i==6:
        print(i)
    else:
        pass    # ignore

for i in range(0,10):
    if i % 2==0:
        print(i)
    else:
        pass


