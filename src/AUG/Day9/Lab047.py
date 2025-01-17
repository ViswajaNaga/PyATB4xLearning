t=tuple()
print(t)

# converting list to tuple

t1=tuple(["ram","sita","rock"])
print(t1) # ('ram', 'sita', 'rock')

# Tuple with in a tuple

boys=("ram","raj")
girls=("sita","suma")
children=(boys,girls)
print(children)   #(('ram', 'raj'), ('sita', 'suma'))
print(children[0])  # ('ram', 'raj')
print(children[1])  # ('sita', 'suma')
print(children[0][0]) # ram
print(children[1][1]) # suma


a,b,c=[1,2,3]

print(a) # 1
print(b) # 2
print(c) # 3

a,b,c=(10,20,30)

print(a) # 10
print(b) # 20
print(c) # 30
