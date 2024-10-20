# Search in tuple

cities=("hyd","delhi","mumbai","chennai")

print("hyd" in cities) # True
print("kolkata" in cities) # False

t=(10,20,30)
# t.append(40) # 'tuple' object has no attribute 'append'

# How to append- covert to list then append and convert back to tuple

my_list=list(t)
my_list.append(40)
t=tuple(my_list)
print(t)

# Concatenation

tu=(4,5,6)
my_tuple=tu + (9,)
print(my_tuple)

my_tuple=tu + (7,8)
print(my_tuple)

env_api_urls=tuple(["dev.com/get","uat.com/post","sit.com/put"])
print(env_api_urls)