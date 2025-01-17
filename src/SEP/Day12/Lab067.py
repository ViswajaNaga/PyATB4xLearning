# global variable can be created outside the class
class Myclass:
    # public variable (instance) # can be used anywhere in the project
    # public variable is created within the class
    public_var = "I am public"
    bankbalance = 1000

    # Private variable - can be used only within the class
    __private_var = 500
    __password = "vish"

    # Protected variable
    _protected_var = "I am protected"
    # protected variable can be used in a same package, and it cannot be used in different package
    b=10
    _c=20
    __d=30

object = Myclass()
print(object.public_var)
print(object.bankbalance)
print(object._protected_var)
print(object.b)
print(object._c)
# print(object.__d)
#
# print(object.__private_var)
# print(object.__password)
