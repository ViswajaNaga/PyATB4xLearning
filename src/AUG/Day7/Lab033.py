def print_arguments(*args):
    # *args = multiple arguments with no limit, -->list
    # print(args[0])
    # to print multiple arguments use for loop
    for i in args:
        print(i)


# this is in the form of list
# list=["john","raj","kaveri","jack"]
print_arguments("john", "raj", "kaveri", "jack")
print_arguments("raj", "kaveri", "jack")
print_arguments("kaveri", "jack", 10, True, False, "LUCKY")
print_arguments() # minimum one argument is important
