# Constructor
# Special function in Class, __init__()
# It will be automatically called whenever you create an object

# purpose of constructor is just to initialize the value no return
# global a=10
class Dog():
    name= None # Instance variable
    age= None
#   color="black" # hardcoded- not generic to all-then what is the use of bluprint?

    def __init__(self,name,age): # Default constructor
        print("I will be automatically called whenever you create an object")
        self.name=name
        self.age=age


    def sleep(self):
        local_variable=10
        print("sleeping")
        print("who is sleeping",self.name,self.age)


dog1=Dog("sunny",2)
print(dog1.name)
print(dog1.age)
#print(dog1.color)
dog1.sleep()
print(id(dog1))

dog2=Dog("bunny",5)
print(dog2.name)
print(dog2.age)
#print(dog2.color)
dog2.sleep()
print(id(dog2))

# print(name) # cannot be used as these are not global variables
# Instance variables can be used by methods/functions

