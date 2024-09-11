# INHERITANCE-# SINGLE Inheritance

class Father:
    key = "2BHK"

    def car(self):
        print("father car!!", "ALTO", self.key)


class Son(Father):
    key2 = "3BHK"

    def home(self):
        print(self.key2)

    def truck(self):
        print("Truck")


Father_obj = Father()
Father_obj.car()

son_obj = Son()
son_obj.car()
son_obj.home()
son_obj.truck()
print(son_obj.key2)

# Father_obj.home() # not possible
# Father_obj.truck() # not possible
# print(Father_obj.key2) # not possible
