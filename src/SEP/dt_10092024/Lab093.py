import math
try:
    math.exp(1000) # OverflowError: math range error
except Exception as e:
    print(e)
    print("please try to use lower exp value")


