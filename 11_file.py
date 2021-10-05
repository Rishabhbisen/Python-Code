# f = open('sample.txt', 'r')
f = open('sample.txt')  # by default r ( reading mode)
data = f.read()
# data = f.read(5)  # first fir character read only
print(data)
f.close()

# other method to read the function
f = open('sample.txt', 'r')
data = f.readline()  # read  first line
print(data)
data = f.readline()  # read  second line
print(data)
data = f.readline()  # read  third line
print(data)


# write file
f = open('good.txt', 'a')
# (w) write file
f.write("hello good mourning this is good.txt file and this is very usful for us")
f.write(" i am appending")  # we can add with the use of (a)
f.write(" good")  # we can add with the use of (a)
f.close()

# with statemant
# if we use this statmant we need not write f.close() function

with open('sample.txt', 'r') as f:
    a = f.read()  # we can read file without the use of f.close()
print(a)

with open('good.txt', 'w') as f:
    # we can write file without the use of f.close()
    f.write(" this is the power of coding")

with open("sample.txt", 'r') as f:
    a = f.read()
if 'rishabh' in a:
    print("rishabh is present in sample.txt")
else:
    print("rishabh is present in sample.txt")
