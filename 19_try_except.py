try:
    print(x)
except:
    print("hello ,good mourning")

try:
    print(x)
except NameError:
    print(" x is not difin")
except:
    print("something went wrong")

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
