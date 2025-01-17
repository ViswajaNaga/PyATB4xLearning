# Method Overriding - Same name in parent and Child
# only Method overriding is present in Python-Run time
# Child always override parent functions
# super means call my parent function
class Grandfather:
    x=100
    def home(self):
        print("Old home")
class Father(Grandfather):
    a=10
    def home(self):
        print("1 BHK")
        print(self.a)
        # print(super().x)


class Son(Father):
    b=20
    def home(self):
        super().home() # this calls Father behaviour(home) by Super() function
        print(super().a)    # this calls Father Attributes(a) by Super() function
        print("No House")
        print(self.b)
        print(super().x)
        # self - me
        # super() - Parent, super class, father

lucky=Son()
lucky.home()