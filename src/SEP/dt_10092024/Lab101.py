# file=open("viswaja.txt","r")
# content=file.read()
# print(content)

try:
    with open("viswaja1.txt","r") as file:
        content=file.readlines()
        print(content)
except FileNotFoundError as FNFE:
    print(FNFE)
finally:
    try:
        file.close()
    except NameError as NE:
        print(NE)




