set1 = set(["ThetestingAcademy", "Academy", "ThetestingAcademy."])
print(len(set1))

for i in set1:
    print(i)

set1.add("vish") #Add an element to a set.  This has no effect if the element is already present.
print(set1)

set1.add("vish")
print(set1)
# Indexation will not work in the set as there is no order in the set
# print(set1[0]) # 'set' object is not subscriptable

