set1 = {1, 2, 3, 3, 4}  # same value is not allow onn set
print(set1)
print(type(set1))

a = {}
print(type(a))  # this is an empty dic

# adding value on empty set
b = ()
print(type(b))  # this is  an empty tuple

c = set()
print(type(c))
c.add(1)
c.add(2)
c.add(3)  # adding a repetivly value cannot be change
c.add(3)
# c.add(3, 4, 5)
print(c)

# accesing elemant
# c.add({1: 2})  # cannot add
# print(c)

print(len(c))
c.remove(3)
print(c)

c.pop()
print(c)

s = {1, '1', 1, 1.1}
print(s)
print(len(s))
