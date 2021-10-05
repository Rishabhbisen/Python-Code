class teacher:  # base class
    def __init__(self, fname, lname, year):
        self.fname = fname
        self.lname = lname
        self.year = year

    def printdata(self):
        print(f"First name is {self.fname}\nSecond name is {self.lname}")


class studant(teacher):  # derived class inherit by base class
    def __init__(self, fname, lname, year):
        # super is a built in function in python we can use teacher
        super().__init__(fname, lname, year)
        # self.graduation_year = 2023   # we can add property in the derived class
        self.graduation_year = year

    def welcome(self):   # we can add method
        print("welcome", self.fname, self.lname,
              " to the class of ", self.graduation_year)


x = studant("rishabh", "rohan", 2023)
x.printdata()
x.welcome()
