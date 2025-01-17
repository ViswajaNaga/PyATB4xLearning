# List
# Collection of Items(duplicate is allowed)

my_list=[10,20,30] # same type of data
my_list2=[10,"viswaja",3.14,False] # different type of data is also allowed

print(my_list)
print(my_list2)

print(len(my_list))
print(len(my_list2))

print(my_list[0])
print(my_list[2])
# print(my_list[10]) # list index out of range exception

my_list[0] = "naga"
my_list[1] = "viswaja"
my_list[2] = "naga"
# my_list[10] = "bala"    # list assignment index out of range exception
print("element at index 0 - ", my_list[0])
print("element at index 1 - ", my_list[1])
print("element at index 2 - ", my_list[2])

print(my_list)

for element in my_list:
    print(element)

for i in range(1,10): # [1,2,3,4,5,6,7,8,9]
    print(i)

print("--------------------------------------------------------")

my_list=[1,2,3]

my_list.append(4)
print(my_list)

# my_list.append(5,6,7) # cannot take multiple ones can take one by one only
my_list.append(5)
my_list.append(6)
my_list.append(7)
print(my_list)
# multiple elements are only allowed when we used extend keyword with the list.

my_list.extend([10,9,8])
print(my_list)

my_list.extend([11])
my_list.extend(["viswaja"])
print(my_list)

#insert()

my_list.insert(0,"naga")
print(my_list)

my_list.insert(-1,"lucky")
print(my_list)
# if we want to replace then we have to reassign the value
# python lists are 0-indexed. So the first element is 0, second is 1, so on.
# So if the there are n elements in a list, the last element is n-1. Remember this!
my_list[1] = "vish"
print(my_list)

print("-----------------------------------")

my_list.remove("naga")
print(my_list)
my_list.remove(2)
print(my_list)
print("-----------------------------------")

my_list_copy=my_list.copy()
print(my_list_copy)
print(my_list)
print("-----------------------------------")
my_list.clear() # because it is cleared here print(my_list) is []
print(my_list_copy)
print(my_list)

#my_list_copy.sort() # not supported between instances of 'int' and 'str'
print(my_list)

my_list_copy.remove("vish")
my_list_copy.remove("lucky")
my_list_copy.remove("viswaja")
print(my_list_copy)

my_list_copy.reverse()
print(my_list_copy)

my_list_copy.sort() # in ascending order
print(my_list_copy)

my_list_copy.sort(reverse=True)
print(my_list_copy)
