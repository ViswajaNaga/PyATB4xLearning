# Custom exception- user defined exception- own exception

class BalanceLowException(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(message)

balance=100
withdraw=int(input("enter the amount"))
if withdraw>balance:
    raise BalanceLowException("balance is low")
else:
    print("remaining balance", balance-withdraw)
