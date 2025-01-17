a = 10


class Person:
    b = 20  # instance variable/class variable-works only with in the class. it belongs to class

    def per_info(self):
        print(self.b) # only for instance variables we use self
        global a  # declare it as global
        a = "hello"
        print(a)


object = Person()
object.per_info()
