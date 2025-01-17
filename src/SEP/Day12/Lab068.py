# private variables can be accessed only through methods with security
class Bank:

    def __init__(self, account_num,balance):
        self.__account_num= account_num # constructor parameter is assigned to private variable
        self.balance=balance

    def deposit(self,amount):
        self.balance= self.balance+amount

    def check_balance(self):
        print(self.balance)
        self.__internal_method() #------this private method can be accessed by public method

    def show_me_account_number(self,is_auth):
        if is_auth==True:
            print(self.__account_num)
        else:
            print("Not allowed")

    def __internal_method(self):
        print("private method")
        print(self.__account_num) # private method can access private variables
        self.show_me_account_number(True) # can access public methods and protected methods also



icici=Bank(234567890,1000)
icici.deposit(100)
icici.check_balance()
icici.show_me_account_number(True)
icici.show_me_account_number(False)
icici.deposit(100)
icici.check_balance()
#icici.__internal_method() # not allowed
#icici.__init__() # not allowed. this is also private method



