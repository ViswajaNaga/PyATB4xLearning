# Multiple Inheritance

class Father:
    key = "ABC"
    __password = 1234

    def __show_password(self):
        print(self.__password)

    def father_money(self):
        return 100

    def home(self):
        return "This is from father"

    def show_everything(self):
        self.__show_password()


class Mother:
    gold = "1kg"

    def mother_money(self):
        return 80

    def home(self):
        return "This is from mother"


class Son(Mother, Father):
    pass


son_obj = Son()
print(son_obj.father_money())
print(son_obj.mother_money())
print(son_obj.home())  # MRO- Method Resolution Order
print(son_obj.gold)

print("===========================================")
son_obj.show_everything()


# one main problem also called as Diamond problem. this problem exists in java but solved in Python
# if father and mother have home() then son_obj.home() will return which home Fathers or mothers
# whichever is the first argument that is considered
# as it is passed as ## class Son(Mother,Father) so Mother home is considered.

class Daughter(Father, Mother):
    pass


daughter_obj = Daughter()
print(daughter_obj.home())
