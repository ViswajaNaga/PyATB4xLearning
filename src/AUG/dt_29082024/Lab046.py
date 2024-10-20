squares = [1, 4, 9, 16, 25]

squares.sort(reverse=True)
print(squares)  # [25, 16, 9, 4, 1]

squares.pop()  # Remove and return item at index (default last).
print(squares)  # [25, 16, 9, 4]

print(squares.pop())  # 4
print(squares)  # [25, 16, 9]

# List is mutable(change) in nature

squares[1] = 50
print(squares)

# TUPLE - Collection of Items

my_tuple = (2, 4, 6, 8, 10)
# my_tuple[1]=12 # IMMUTABLE(cannot change) in nature
print(my_tuple)  # 'tuple' object does not support item assignment

# Tuple - If the list is not changing use TUPLE
# List - If the list is changing use LIST

# tuple can be converted to list and list can be converted to tuple
# tuple is faster compared to list
my_tuple = ("tta.com", "sdet.live")
print(my_tuple)
my_tuple_list = list(my_tuple)
print(my_tuple_list)

my_tuple_new=tuple(my_tuple_list)
print(my_tuple_new)

# Real case - If we know the data is fixed and it will not change then we can use tuple to save the memory

