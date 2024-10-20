# Understanding Decorators in Python.

def add_extra_security(func):
    def wrapper():
        print("Before the function is called")
        print("helmet","gloves","shoes")
        func()
        print("After the function is called")
        print("safe driving")

    return wrapper()

@add_extra_security
def scooty_driving():
    print("I am driving")
