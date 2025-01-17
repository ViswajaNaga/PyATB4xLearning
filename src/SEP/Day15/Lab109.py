# deque - double-ended queue
# FIFO-FirstIn FirstOut- Bus stand Queue, Airport Queue
# A list-like sequence optimized for data accesses near its endpoints

from collections import deque

# create a deque
# d=deque()
d=deque([1,2,3])
print(d)

d.append(4) # adds an item through append
print(d)

# advantage of deque is we can add elements double-sided (both left and right side)

# add an element on the left
d.appendleft(0)
print(d)

# extend(list) the deque
d.extend([5])
print(d)

d.extend([6,7])
print(d)

print(d.pop()) # removes from right
print(d.popleft()) # removes from left
print(d)

d.reverse()
print(d)

