from src.SEP.Day11.Lab060 import print_details060

print_details060()

# always create python packages instead of normal dir
# import is possible in python package and not normal directory
# cross calling of functions is possible

def print_details061():
    print("I am from lab061")
    print_details060()

print_details061()

