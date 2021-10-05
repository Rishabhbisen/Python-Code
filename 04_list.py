# list
list1 = [1, 23, 4, 56, 4]
print(list1)  # this is an list
list1.append("good mourning")
print(list1)

lis2 = [23, "rishabh ", 5.67]
print(lis2)
print(lis2[2])
lis2[0] = 65  # add number on list
print(lis2)

# list slicing

l1 = ['hello', 'good', 45, 657.7]
print(l1[:1])   # slicing list

# list method
l2 = [34, 67, 23, 5, 6, 678, "gpp"]
# l2.sort()
# l2.count(67)
# l2.reverse()
# l2.insert(34, 111)
# l2.pop(3)
# l2.remove("gpp")
# del l2  # this will show a error
print(l2.clear())

# loop list
this_list = ['apple', 'banana', 'mango', 'go']
for a in this_list:
    print(a, end=", ")

i = 0
while i < len(this_list):
    print(this_list[i])
    i = i+1

newlist = [x.upper() for x in this_list]
print(newlist)

newgo = []
for x in this_list:
    if 'a' in x:
        newgo.append(x)
print(this_list)


print(this_list.copy())   # copy list on perticular list

g1 = [1, 2, 3, 4, ]
g2 = ['good', 'god', 'goodies']

g3 = g1+g2
print(g3)

for x in g1:
    g2.append(x)
print(g2)
