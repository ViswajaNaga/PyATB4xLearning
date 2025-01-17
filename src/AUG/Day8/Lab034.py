# MAKE PIZZA

def make_pizza(*toppings):
    for topin in toppings:
        print(topin)


vish = make_pizza("tomato")
chinnu = make_pizza("panner", "mushroom", "onion")
bala = make_pizza("olives", "capsicum", "sweetcorn")


# MAKE PIZZA with base

def make_pizza(*toppings,base):  # two arguments with * not allowed and * should be for 1st argument only
        print(toppings,base)

make_pizza("panner", "mushroom", "onion",base="thin crust")