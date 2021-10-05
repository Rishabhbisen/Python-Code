class number:
    def sum(self):
        return self.a+self.b


num = number()
num.a = 12
num.b = 13
s = num.sum()
print(s)


class railwayform:
    def printdata(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")


rishabhapplication = railwayform()
rishabhapplication.name = "rishabh"
rishabhapplication.train = "rajdhani"
# rishabhapplication.printdata()
r = rishabhapplication.printdata()  # both are right
# print(r)


class employ:
    company = "google"
    salary = 50000
    address = "agarwada"


rishabh = employ()
rishi = employ()

# rishabh.salary = 400000
# rishi.salary = 30000

print(rishabh.company)
print(rishi.company)
employ.company = "youtube"
rohan = employ()
soham = employ()
print(rohan.company)
print(soham.company)
print(rishabh.salary)
print(rishi.salary)
print(rishi.address)
