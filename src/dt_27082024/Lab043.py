# lambda expression
# A lambda is an anonymous function that returns some form of data

def triple_me(num):
    return num * 3


op = triple_me(10)
print(op)

# Any function can be converted into one-liner using lambda

op = lambda num: num * 4
print(op(10))

o = lambda n: n+10
print(o(100))

oo = lambda a,b: a*b
print(oo(3,4))

op = lambda a,b,c : a+b+c
print(op(2,3,4))

def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

even_odd(7)


output= lambda num : "even" if num%2==0 else "odd"
print(output(4))
