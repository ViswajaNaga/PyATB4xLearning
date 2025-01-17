# try, except and finally
# file
import os

try:
    file = open('testdata.txt', 'r')
    print(file.read())
except FileNotFoundError as FNFE:
    print(FNFE)
    print("Fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as NE:
        print(NE)

# If we don't know any type of exception then we will call the father(Exception)

# to find the path where file is present
fullpath = os.getcwd()
print(fullpath)
fullpath_file = fullpath + "example.txt"
print(fullpath_file)

print(os.getcwd())
