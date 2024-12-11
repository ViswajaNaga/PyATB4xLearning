# Calling function within function

def outer_fun():
    x = 10  # local integer variable

    def inner_fun1():
        print(x)

    def inner_fun2():
        print(x)

    inner_fun1()
    inner_fun2()

outer_fun()
