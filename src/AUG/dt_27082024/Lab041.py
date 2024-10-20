# @staticmethod
# @classmethod
# @property
# @functools.wraps

# the above decorators are used in OOPs concepts
# Chaining Decorators

def decorator1(func):
    def wrapper():
        print("decorator1")
        func()
    return wrapper()

def decorator2(func):
    def wrapper():
        print("decorator2")
        func()
    return wrapper()

@decorator1
@decorator2
def greet():
    print("Hello")
