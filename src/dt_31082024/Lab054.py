class Dog: # class name always start with capital letter
    #A
    name= None
    breed= None
    color= None

    #B
    def sleep(self):
        print("sleeping")

    def bark(self):
        print("barking")

    def eat(self,food):
        print(food)


dog1=Dog()
print(dog1.name)  # how to set the value automatically instead of None-this can be done using constructor
dog1.name="bunny"
print(dog1.name)
dog1.sleep()

dog2=Dog()
print(dog2.name)
dog2.name="cutie"
print(dog2.name)
dog2.bark()
dog2.eat("biscuits")

