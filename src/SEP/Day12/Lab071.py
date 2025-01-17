# Multilevel Inheritance

class Grandfather:
    silver="1kg"

    def BHK1(self):
        print("1 BHK")

class Father(Grandfather):
    gold="500gm"

    def BHK2(self):
        print("2 BHK")


class Son(Father):
    Diamond = "diamond"

    def BHK3(self):
        print("3 BHK")

s=Son()
f=Father()
gf=Grandfather()

s.BHK1()
s.BHK2()
s.BHK3()
print(s.silver)
print(s.gold)
print(s.Diamond)
