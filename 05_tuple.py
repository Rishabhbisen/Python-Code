a = (1, 2, 3, 'good', 'know')
print(a)
print(type(a))
print(len(a))
print(a[1])  # access tuple
print(a[:2:3])
if 'good' in a:
    print(' yes ')
# update tuple
x = ['hello', 'good', 'know']
y = list(x)
y[1] = "hoooo"
# firstly we change tuple into list and than process all the things
y.append('orrange')
x = tuple(y)
print(x)

# unpack tuple
good = (' come', 'gone ', 'very ', 'buzy')
(hello, green, *chalo) = good
print(hello)
print(green)
print(chalo)

fruit = [1, 2, 45, 5]
mytuple = fruit*2
print(mytuple)
print(mytuple.count(2))
