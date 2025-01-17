# Web automation - selenium- PAGE OBJECT MODEL
# Page- You are going to automate

class VMOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "viswaja36@gmail.com" and self.password == 1234:
            print("Allowed to login")
        else:
            print("Not allowed")

email=input("enter email")
password=int(input("enter password"))
vwo_obj = VMOLoginPage(email, password)
vwo_obj.login_confirm()

print("======================================================")

vwo_obj = VMOLoginPage("ram@gmail.com", 1234)
vwo_obj.login_confirm()
