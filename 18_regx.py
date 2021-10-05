import re
x = " today is raining in our village"
y = re.search("today ", x)
if y:
    print("yes , matched")
else:
    print(" No, does not matched")

u = " the rain in spain"
u = re.split("\s", u)
print(u)
