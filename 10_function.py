def my_func():
    print(" hello from a function")


my_func()


def fun(fname):
    print(fname+"refrance")


p = fun("email ")
print(p)
fun("goal ")
fun("linux ")


def myfun(fname, lname):
    print(fname + lname)


myfun("Rishabh ", " Bisen")
myfun("Is a  ", " good boy")


def name(*kid):
    print(" youngest kid is ", kid[2])


name("rishabh", "rohit", "yuvan")


def mu(country="norway"):
    print(" my country is "+country)


mu()
mu("india")
mu("america")
mu("brazil")


def leetcode(food):
    for x in food:
        print(x)


fruit = ['aplle', 'bannan', 'mangos']
leetcode(fruit)


def codesafe(x):
    return x*5


print(codesafe(5))
print(codesafe(7))
print(codesafe(6))
p = codesafe(4)
print(p)
