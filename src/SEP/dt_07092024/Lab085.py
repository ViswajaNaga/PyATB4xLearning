from abc import ABC, abstractmethod

class PyATB(ABC):
    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Student(PyATB):

    def payfee(self):
        # print("Fee paid")
        pass

vish=Student()
vish.payfee()
vish.enrolled()
