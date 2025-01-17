# Match statement--similar to switch in JAVA (works in python >3.10)

# match variable:
#     case pattern1:
#         code block
#     case pattern2:
#         code block

# write a program to ask the user which browser he want to run automation

browser_name= input("enter browser name\n")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        print("execute firefox code")
    case "chrome":
        print("execute chrome code")
    case "edge":
        if browser_name=="edge":
            print("HELLO")
        print("execute edge code")
    case _:  # _ is the default condition to be used in match statement
        print("browser not found")
# if statement can be used within the case
# no need to use break statement in MATCH but break is used in Switch statement in Java


user_type= input("Enter the user_type manager,guest,admin")

match user_type:
    case "admin" | "manager":
        print("hello sir")
    case "guest":
        print("hello, guest")
    case _:
        print("hello, there")