# SET - collection of unique elements {} --> used to remove duplicates
# order is not considered in set

list_of_unique_items={1,2,3,4,4,5,5}
print(list_of_unique_items) # {1, 2, 3, 4, 5}
# to remove duplicates in a list - convert to set first and remove duplicates

list1=[43.5,12,78,78,12]
set1=set(list1)
print(set1)

tuple1=("apple","banana","apple")
print(tuple1)
print(set(tuple1))