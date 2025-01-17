# Hierarchial Inheritance

class Father:

    def BHK1(self):
        print("1 BHK")

class Chinnu(Father):

    def BHK2(self):
        print("2 BHK")


class Lucky(Father):

    def BHK3(self):
        print("3 BHK")

chinnu_obj=Chinnu()
chinnu_obj.BHK2()
chinnu_obj.BHK1()

lucky_obj=Lucky()
lucky_obj.BHK3()
lucky_obj.BHK1()
#lucky_obj.BHK2() # cannot access it belongs to chinnu


