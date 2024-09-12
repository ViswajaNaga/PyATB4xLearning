# Abstraction-OOPS
# hiding the details and showing what is required
# abstract actual meaning is incomplete
# to create incomplete method we have to inherit ABC class

from abc import ABC,abstractmethod

class Father(ABC):
    def __init__(self,amount):
        self.amount=amount
    @abstractmethod
    def loan(self):
        pass

class Son(Father):

    def loan(self):
        print("Loan Paid")

Lucky=Son("1L")   # we cannot create object of Son until loan is paid
Lucky.loan()
