# hiding the classes by using abstractmethod / abstractclassmethod by using ABC
#
#from abc import ABC, abstractmethod

class Engine:

    def start(self):
        pass

    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def drive(self):
        self.start()
        print("I am driving")
        self.stop()

c=Car()
c.drive()

print("================================")

from abc import ABC, abstractmethod
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def drive(self):
        self.start()
        print("I am driving")
        self.stop()

c=Car()
c.drive()



