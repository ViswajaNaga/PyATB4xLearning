# OrderedDict

from collections import OrderedDict, defaultdict

d = {"name": "vish", "age": 30, "address": "HYD", "id": 123, "branch": "EEE"}
## In a normal dictionary order is not maintained
print(d)

d = dict()
d["name"] = "lucky"
d["age"] = 1
d["DOB"] = "march"
print(d)
## In OrderedDictionary order is maintained


od = OrderedDict()
od["banana"] = 6
od["apple"] = 3
od["jackfruit"] = 1
print(od)


dd = defaultdict(int)
print(dd)
# why we use data structures?
# data structures are used to store data, update, search, manipulate etc(list,tuple,set,dict)
# to store only unique names- use set
# use key value pairs in order-ordered dict


