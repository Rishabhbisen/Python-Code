i = 0
while i <= 5:
    print(i)
    i = i+1
print(' Done')

i = 1
while i <= 50:
    print(i)
    i = i+1
print('done')

# print list using while loop
fruit = ['mango', 'apple', 'banan', 'annar']
i = 0
while i < len(fruit):
    print(fruit[i], end=' ,')
    i = i++1
if 'mango' in fruit:  # this is if condition in loops
    print('yes')

# for loop
l1 = ['go', 'come', 'fast', 'with']
for i in l1:
    print(i)


for i in range(1, 8, 2):
    print(i)

for i in range(10):
    print(i)
else:
    print('all process is done')

for j in range(10):
    print(j)
    if j == 5:
        break
else:
    print('done')

for o in range(10):
    print(o)
    if i == 4:
        continue
else:
    print('all is done')

for t in range(5):
    print(t)
    if t < 0:
        pass
else:
    print('all process is done')

num = int(input('Enter number \n'))
for u in range(1, 11):
    # print(u*num)  # this is the first way
    print(f"{num} x {u} = {num*u}")

l2 = ['Rishabh', 'Rohit', 'yuvan', 'vikash']
for name in l2:
    if name.startswith('R'):
        print(name)

# how to get factorial using loop
num = int(input('Enter number\n'))
factorial = 1
for p in range(1, num+1):
    factorial = factorial*p
print(' factorial of ', num, 'is', factorial)  # this is the first way
print(f" the factorial of {num} is {factorial}")

# this is the other method how to get a single num of factorial
num = 5
fact = 1
for i in range(1, 5+1):
    fact = fact*i
print(fact)

for i in range(4):
    print('*'*(i+1))
