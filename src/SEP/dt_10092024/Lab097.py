import os

# operating system module - files, path related to OS
print(os.name)  # nt for windows
# posix - unix based system - mac and linux

if os.name == "posix":
    print("using mac")
else:
    print("windows")

print(os.getcwd())
os.chdir("C:\\Users\\Balakrishna\\OneDrive\\Documents")
print(os.getcwd())
# os.mkdir("new_directory") # a folder by name new_directory is created in the above path(Documents)
os.chdir("C:/Users/Balakrishna/PycharmProjects/PyATB4xLearning/src/SEP/dt_10092024")
print(os.getcwd())
# os.makedirs('parent/child/grandchild') # created a parent directory, inside it child is created ,
# and inside child grandchild is created
print(os.listdir('.'))  # A list is created

for file in os.listdir('.'):
    print(file)

# os.remove('example.txt') # got removed from directory
# os.mkdir("new_directory") # folder new_directory is created
# os.rmdir("new_directory") # above created folder is removed
# os.rename('example.txt','testdata.txt')

# full_path=os.path.join('folder','file.txt')
# full_path = os.path.join("C:\Users\Balakrishna\PycharmProjects\PyATB4xLearning\src\SEP\dt_10092024", "testdata.txt")
# print(full_path)

print(os.path.exists("testdata.txt")) #True
print(os.path.isfile("testdata.txt")) #True
print(os.path.isdir("parent")) #True
print(os.path.isdir("parents")) #True

