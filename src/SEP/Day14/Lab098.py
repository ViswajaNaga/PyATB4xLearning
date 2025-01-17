# Try and except can be used within the class also
class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int only for value of a")
        else:
            print(a)
        finally:
            print("FINALLY : Anyhow I will be printed")

x = XYZ()
x.f1()