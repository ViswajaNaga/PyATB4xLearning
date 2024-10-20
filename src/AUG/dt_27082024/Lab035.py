# Functions scope-global and local

pb_global = 1000


def myfun():
    pv_local = 20
    print(pv_local)
    pb_global = 99
    print(pb_global)  # Local variables have more preference as compared to global variables.


print(pb_global)
myfun()

print(pb_global)


def f1():
    print(pb_global)


f1()
